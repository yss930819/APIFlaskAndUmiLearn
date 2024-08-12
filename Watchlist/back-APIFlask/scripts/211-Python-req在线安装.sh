#! /bin/bash

echo "启动虚拟环境"
. ./venv/Scripts/activate 

echo "安装依赖文件"
pip install -r requirements.txt
