#! /bin/bash

echo "启动虚拟环境"
. ./venv/Scripts/activate 


echo "读取 requirements.txt 下载离线 whl"
pip wheel --wheel-dir=wheelhouse -r requirements.txt
