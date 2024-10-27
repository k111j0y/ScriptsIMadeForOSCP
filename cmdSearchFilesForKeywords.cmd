@echo off
setlocal enabledelayedexpansion

:: cmdSearchFilesForKeywords.cmd "C:\Dir\Ya\Wanna\Search" FirstKeyword NextKeywordIsOptional ThirdKeywordIsOptionalETC


if "%~1"=="" (
    echo Indicate a path to search.
    exit /b
)

if "%~2"=="" (
    echo There must be at least one keyword to search for.
    exit /b
)

set "directory=%~1"
shift

:: Loop through the rest of the arguments as keywords
set "keywords="
:loop
if "%~1"=="" goto search
set "keywords=!keywords! /C:"%~1""
shift
goto loop

:search
:: Loop through each file in the directory recursively
for /r "%directory%" %%f in (*) do (
    :: Search the file for any of the keywords (case-insensitive with /i)
    findstr /i %keywords% "%%f" >nul
    if !errorlevel! equ 0 (
        echo Keyword found in file: %%f
    )
)

endlocal
