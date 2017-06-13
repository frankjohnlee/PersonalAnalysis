@echo off

if NOT "%1"=="-libnames" goto notlibnames
    echo libdynd.lib;libdyndt.lib
    exit /B 0
:notlibnames

if NOT "%1"=="-libdir" goto notlibdir
    REM This batch file should be in a ...\bin relative to ...\lib
    pushd %~f0\..\..\lib
    echo %CD%
    popd
    exit /B 0
:notlibdir

if NOT "%1"=="-includedir" goto notincludedir
    REM This batch file should be in a ...\bin relative to ...\include
    pushd %~f0\..\..\include
    echo %CD%
    popd
    exit /B 0
:notincludedir

if NOT "%1"=="-rootdir" goto notrootdir
    REM This batch file should be in a ...\bin relative to ...\include
    pushd %~f0\..\..
    echo %CD%
    popd
    exit /B 0
:notrootdir

if NOT "%1"=="-version" goto notversion
    echo 747e8b1
    exit /B 0
:notversion

echo Usage: %0 OPTION
echo Print information for linking libdynd.
echo
echo Options:
echo   -libnames    Prints a semicolon separated list of the library names.
echo   -libdir      Prints the full path of the directory containing the libraries.
echo   -includedir  Prints the directory with the libdynd include files.
echo   -version     Prints the version of libdynd.
exit /B 1
