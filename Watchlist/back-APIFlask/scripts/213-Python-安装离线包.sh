#! /bin/bash

echo "启动虚拟环境"
. ./venv/Scripts/activate 

wheelhouse="./wheelhouse"
if [ ! -d $wheelhouse ]; then
    echo "文件夹不存在!"
    exit 255
fi

echo "读取 requirements.txt 安装离线 whl"
pip install --no-index --find-links=wheelhouse -r requirements.txt
