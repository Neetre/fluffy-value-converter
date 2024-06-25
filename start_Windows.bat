@ECHO OFF

CALL ./setup/setup_Windows.bat

CLS

REM Change directory to 'bin' and run the application
CD /d bin
IF ERRORLEVEL 1 (
    ECHO Failed to change directory to 'bin'
    PAUSE
    EXIT /B 1
)

SET /P UserInput="Do you want to run the program in GUI mode? (y/n)":
IF /I "%UserInput%" EQU "y" GOTO GUI
IF /I "%UserInput%" EQU "n" GOTO CLI

:GUI
python converter.py --gui
IF ERRORLEVEL 1 (
    ECHO Failed to run converter.py
    EXIT /B 1
)
GOTO End


:CLI
python converter.py --cli
IF ERRORLEVEL 1 (
    ECHO Failed to run converter.py
    EXIT /B 1
)
GOTO End


:End
EXIT /B 0