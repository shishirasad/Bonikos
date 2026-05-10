import argparse
import secrets
from pathlib import Path

from backend import models
from backend.database import DATA_DIR, SessionLocal
from backend.app.domains.platform.security import get_password_hash


RESET_OUTPUT_FILE = Path(DATA_DIR) / "admin_password_reset.txt"


def reset_admin_password(username: str, password: str | None = None) -> str:
    db = SessionLocal()
    try:
        user = db.query(models.User).filter(models.User.username == username).first()
        temporary_password = password or secrets.token_urlsafe(10)

        if user:
            user.password_hash = get_password_hash(temporary_password)
            user.is_active = True
            if username == "owner":
                user.role = "Admin"
            action = "updated"
        else:
            user = models.User(
                username=username,
                role="Admin",
                password_hash=get_password_hash(temporary_password),
                is_active=True,
            )
            db.add(user)
            action = "created"

        db.commit()
        RESET_OUTPUT_FILE.write_text(
            "\n".join(
                [
                    "Temporary admin reset credentials",
                    f"username: {username}",
                    f"password: {temporary_password}",
                    "note: sign in and change this password immediately.",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        return action
    finally:
        db.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Reset or recreate an admin login with a fresh temporary password.")
    parser.add_argument("--username", default="owner", help="Admin username to reset. Default: owner")
    parser.add_argument("--password", default=None, help="Optional password. If omitted, a secure temporary password is generated.")
    args = parser.parse_args()

    action = reset_admin_password(args.username.strip() or "owner", args.password)
    print(f"Admin credentials {action}.")
    print(f"Temporary password saved to: {RESET_OUTPUT_FILE}")


if __name__ == "__main__":
    main()
