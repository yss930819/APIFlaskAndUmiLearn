# 此脚本用于判断系统是否为 wsl 系统或者 使用的 windows 上的 git bash
# 所有脚本都应该先包含此脚本用于初始化命令参数

if [ -z "${COMMON_INIT}" ]; then

# 这里定义了公共的函数
COMMON_INIT=1

LONG_SIGN="=============="
SHOT_SIGN="=="

printLong() {
  echo ${LONG_SIGN} "$*" ${LONG_SIGN}
}


printShort() {
  echo ${SHOT_SIGN} "$*" 
}

error() {
  echo "ERROR " "$*"
  exit 1
}

warning() {
  echo "Warning " "$*"
  HAS_WARNING="warning"
}

checkTool() {
  which $1 | grep -qE "$1" && return 0 || return 1
}

recordStartTime(){
  startTime=$(date +%Y%m%d-%H:%M:%S)
  startTime_s=$(date +%s)
}

recordEndTime(){
  endTime=$(date +%Y%m%d-%H:%M:%S)
  endTime_s=$(date +%s)

  sumTime=$(( endTime_s - startTime_s ))
 
  printShort "时间：${startTime} ---> ${endTime}" "总耗时: ${sumTime} 秒"
}


printLong "初始化"

# 下面是对 WSL 的处理
CMD_SUFFIX=""

SYSTEM_INFO=$(uname -rs) 
printShort "系统信息" ${SYSTEM_INFO}

if  echo ${SYSTEM_INFO} | grep -qEo "Linux.*[Mm]icrosoft"
then
  echo "**正在 Windows linux 子系统执行操作, 为所有命令增加 .exe 后缀**";
  CMD_SUFFIX=".exe"
fi

# 获取项目名称
PROJECT_PATH=$(pwd)
PROJECT_NAME=$(basename ${PROJECT_PATH})


fi