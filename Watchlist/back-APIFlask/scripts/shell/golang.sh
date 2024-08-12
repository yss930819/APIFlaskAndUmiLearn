# 这里对 GO 的参数进行初始化

if [ -z "${GO_INIT}" ]; then

    GO_INIT="init"

    GO=go${CMD_SUFFIX}
    GO_SUPPORTED_VERSIONS="1.16|1.17|1.18" # 支持的 go 版本目前定义为 1.16 之后

    # 判断 GO 版本
    # go.exe version | grep -q -E '\bgo(1.16|1.17)\b' && echo 0 || echo 1
    GO_VERSION=$(${GO} version | grep -Eo "\bgo(${GO_SUPPORTED_VERSIONS})\.[0-9]+\b")
    if test -z ${GO_VERSION}
    then
        error "不支持您的 go 版本, 请安装下述版本: '${GO_SUPPORTED_VERSIONS}'"
    fi

    # 信息输出
    printShort "GO版本: " ${GO_VERSION}

fi