@echo off

PUSHD %~DP0 & cd /d "%~dp0"
%1 %2
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :runas","","runas",1)(window.close)&goto :eof

:runas

@REM 填写自己的脚本

set ENV_PARAM=XXXXX

echo 安装环境变量 %ENV_PARAM% %~dp0
setx "%ENV_PARAM%" %~dp0 /m
pause

