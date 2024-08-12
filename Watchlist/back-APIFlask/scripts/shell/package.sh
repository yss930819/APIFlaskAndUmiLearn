#! /bin/bash
if [ -z "${PACKAGE_INIT}" ]; then

    # 获取 项目相关参数
    # WORK_PATH=$(pwd)
    # cd "../../"
    # . ./scripts/shell/common.sh
    # . ./scripts/shell/project.sh
    # cd "$WORK_PATH" || exit
    # 读取项目配置
    PACKAGE_INIT=1
fi