@echo off
setlocal

rem Remove the existing code_uri directory if it exists
if exist code_uri (
    rmdir /s /q code_uri
)

rem Create a new code_uri directory and subdirectories
mkdir code_uri
mkdir code_uri\chatytt

rem Copy chatytt and server directories into code_uri
xcopy ..\chatytt\. code_uri\chatytt\ /E /I /H /Y
xcopy ..\server\. code_uri\server\ /E /I /H /Y

rem Export requirements.txt using Poetry
call poetry export --without-hashes -f requirements.txt --output requirements.txt
move requirements.txt code_uri\

endlocal
