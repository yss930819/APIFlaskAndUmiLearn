if [ -z "${TOOL_INIT}" ]; then

TOOL_INIT="init"

GIT_CHGLOG=git-chglog${CMD_SUFFIX}
YS_CLI=ys-cli${CMD_SUFFIX}
GF=gf${CMD_SUFFIX}
GIT=git${CMD_SUFFIX}

toolCheckAndInstall() {
    printShort "检查 " $1 
    checkTool $1
    if [ $? != 0 ]
    then
        echo "正在安装..."
        ${GO} get $2
        if [ $? != 0 ]
        then
            warning "安装失败" $1 "×"
        fi
    else
        echo "已安装 √"
    fi
    return 0
}

fi