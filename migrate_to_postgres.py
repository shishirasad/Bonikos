import argparse
from collections.abc import Iterable

from sqlalchemy import Integer, create_engine, inspect, select, text
from sqlalchemy.engine import Connection

from backend import models  # noqa: F401
from backend.database import DEFAULT_SQLITE_URL, Base, normalize_database_url


def build_engine(database_url: str):
    engine_kwargs: dict = {"pool_pre_ping": True}
    if database_url.startswith("sqlite"):
        engine_kwargs["connect_args"] = {"check_same_thread": False}
    return create_engine(database_url, **engine_kwargs)


def copy_table_rows(source_conn: Connection, target_conn: Connection, table_name: str, batch_size: int = 500) -> int:
    table = Base.metadata.tables[table_name]
    result = source_conn.execute(select(table))
    copied = 0

    while True:
        batch = result.mappings().fetchmany(batch_size)
        if not batch:
            break
        payload = [dict(row) for row in batch]
        target_conn.execute(table.insert(), payload)
        copied += len(payload)

    return copied


def clear_target_database(target_conn: Connection) -> None:
    if target_conn.dialect.name == "postgresql":
        for table in reversed(Base.metadata.sorted_tables):
            target_conn.execute(text(f'TRUNCATE TABLE "{table.name}" RESTART IDENTITY CASCADE'))
        return

    for table in reversed(Base.metadata.sorted_tables):
        target_conn.execute(table.delete())


def reset_postgresql_sequences(target_conn: Connection) -> None:
    if target_conn.dialect.name != "postgresql":
        return

    for table in Base.metadata.sorted_tables:
        integer_pk_columns = [
            column
            for column in table.primary_key.columns
            if isinstance(column.type, Integer)
        ]
        if len(integer_pk_columns) != 1:
            continue

        pk_column = integer_pk_columns[0]
        max_value = target_conn.execute(
            text(f'SELECT COALESCE(MAX("{pk_column.name}"), 0) FROM "{table.name}"')
        ).scalar_one()

        sequence_name = target_conn.execute(
            text("SELECT pg_get_serial_sequence(:table_name, :column_name)"),
            {
                "table_name": table.name,
                "column_name": pk_column.name,
            },
        ).scalar_one_or_none()

        if not sequence_name:
            continue

        if max_value and int(max_value) > 0:
            target_conn.execute(
                text("SELECT setval(to_regclass(:sequence_name), :value, true)"),
                {
                    "sequence_name": sequence_name,
                    "value": int(max_value),
                },
            )
        else:
            target_conn.execute(
                text("SELECT setval(to_regclass(:sequence_name), 1, false)"),
                {
                    "sequence_name": sequence_name,
                },
            )


def ordered_table_names() -> Iterable[str]:
    for table in Base.metadata.sorted_tables:
        yield table.name


def migrate(source_url: str, target_url: str) -> None:
    source_engine = build_engine(source_url)
    target_engine = build_engine(target_url)

    if not target_url.startswith("postgresql"):
        raise RuntimeError("Target database must be PostgreSQL.")

    Base.metadata.create_all(bind=target_engine)

    source_inspector = inspect(source_engine)
    source_tables = set(source_inspector.get_table_names())

    with source_engine.connect() as source_conn, target_engine.begin() as target_conn:
        clear_target_database(target_conn)
        for table_name in ordered_table_names():
            if table_name not in source_tables:
                print(f"{table_name}: skipped (not present in source)")
                continue
            copied = copy_table_rows(source_conn, target_conn, table_name)
            print(f"{table_name}: {copied} rows copied")
        reset_postgresql_sequences(target_conn)


def main() -> None:
    parser = argparse.ArgumentParser(description="Copy the local SQLite application data into a PostgreSQL database.")
    parser.add_argument(
        "--source",
        default=DEFAULT_SQLITE_URL,
        help=f"Source SQLAlchemy database URL. Default: {DEFAULT_SQLITE_URL}",
    )
    parser.add_argument(
        "--target",
        required=True,
        help="Target PostgreSQL SQLAlchemy URL.",
    )
    args = parser.parse_args()

    source_url = normalize_database_url(args.source)
    target_url = normalize_database_url(args.target)

    print(f"Source: {source_url}")
    print(f"Target: {target_url}")
    migrate(source_url, target_url)
    print("Migration completed.")


if __name__ == "__main__":
    main()
