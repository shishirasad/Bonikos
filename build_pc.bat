@echo off
echo Building MY BUSINESS for Production...

:: Build Frontend
cd frontend
echo Building Frontend Assets...
call npm run build

:: Build PC App (Tauri)
echo Building Desktop Application (MSI/EXE)...
call npm run tauri build

echo Build Complete. Check 'frontend\src-tauri\target\release\bundle' for your installer.
pause
