@echo off

PUSHD %~DP0 & cd /d "%~dp0"
%1 %2
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :runas","","runas",1)(window.close)&goto :eof

:runas

@REM ��д�Լ��Ľű�

set ENV_PARAM=XXXXX

echo ��װ�������� %ENV_PARAM% %~dp0
setx "%ENV_PARAM%" %~dp0 /m
pause

