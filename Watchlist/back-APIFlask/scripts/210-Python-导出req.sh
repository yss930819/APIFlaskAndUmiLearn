#! /bin/bash

echo "启动虚拟环境"
. ./venv/Scripts/activate 

echo "导出依赖文件"
pip freeze > requirements.txt
