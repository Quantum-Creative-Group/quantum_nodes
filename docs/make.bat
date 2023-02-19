@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%2" == "" (
	set SPHINXBUILD=sphinx-build
) else (
	set SPHINXBUILD=%2
)

set SOURCEDIR=source
set BUILDDIR=build
set MODULE=quantum_nodes

if "%1" == "" goto help

move "../%MODULE%/__init__.py" "../%MODULE%/___init__.py"
powershell -ExecutionPolicy ByPass -command ". replace_matching_string_in_files.ps1 -find '@persistent' -replace '#@persistent';"

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

powershell -ExecutionPolicy ByPass -command ". replace_matching_string_in_files.ps1 -find '#@persistent' -replace '@persistent';"
move "../%MODULE%/___init__.py" "../%MODULE%/__init__.py"
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
