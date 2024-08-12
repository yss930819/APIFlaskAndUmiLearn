#! /bin/bash

. ./scripts/shell/common.sh
. ./scripts/shell/golang.sh
. ./scripts/shell/tool.sh

if [ -z "${VERSION_INIT}" ]; then
VERSION_INIT="init"

printShort "获取版本号"

readVersion(){
  VERSIONS_PATTERN="[0-9]+\.[0-9]+\.[0-9]+"

  LAST_VERSION=$(${GIT} log --grep=version: --pretty=tformat:"%h %s %(describe)" | awk '{if(NR==1){printf "%s",$3}}')
  LAST_MAJOR=$(echo "${LAST_VERSION}" | grep -Eo "${VERSIONS_PATTERN}" | awk -F. '{print $1}')
  LAST_MINOR=$(echo "${LAST_VERSION}" | grep -Eo "${VERSIONS_PATTERN}" | awk -F. '{print $2}')
  LAST_PATCH=$(echo "${LAST_VERSION}" | grep -Eo "${VERSIONS_PATTERN}" | awk -F. '{print $3}')

  IS_OK=FALSE

  while [[ "${IS_OK}" == "FALSE" ]]
  do
    echo "请输入版本(上一版本为：${LAST_VERSION}):"
    read -r VERSION
    MAJOR=$(echo "${VERSION}" | grep -Eo "${VERSIONS_PATTERN}" | awk -F. '{print $1}')
    MINOR=$(echo "${VERSION}" | grep -Eo "${VERSIONS_PATTERN}" | awk -F. '{print $2}')
    PATCH=$(echo "${VERSION}" | grep -Eo "${VERSIONS_PATTERN}" | awk -F. '{print $3}')

    if [ "${MAJOR}" -gt "${LAST_MAJOR}" ]
    then
      IS_OK="TRUE"
    elif [ "${MAJOR}" -eq "${LAST_MAJOR}" ] && [ "${MINOR}" -gt "${LAST_MINOR}" ]
    then
      IS_OK="TRUE"
    elif [ "${MAJOR}" -eq "${LAST_MAJOR}" ] && [ "${MINOR}" -eq "${LAST_MINOR}" ] && [ "${PATCH}" -gt "${LAST_PATCH}" ]
    then
      IS_OK="TRUE"
    else
      echo "输入版本号不正确！"
    fi
  done

  if [[ "${VERSION}" != v* ]]
  then
    echo "缺少 v 字母"
    VERSION="v${VERSION}"
  fi
}

# 判断是不是使用默认方式生成版本号
if [ -z "${VERSION_DEFAULT}" ]; then
  readVersion
else
  VERSION="$(git describe)-${VERSION_DEFAULT}"
fi

echo "版本号: ${VERSION}"

fi