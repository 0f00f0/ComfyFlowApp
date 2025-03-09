#!/bin/bash

# get current path
CUR_DIR="$(cd "$(dirname "$0")" && pwd)/$(basename "$0")"
PROJECT_PATH=$(dirname $(dirname "$CUR_DIR"))
echo "$PROJECT_PATH"
cd $PROJECT_PATH

# set LOGURU_LEVEL to ERROR
export LOGURU_LEVEL=INFO

export STREAMLIT_SERVER_PORT=8501
# set COMFYFLOW_API_URL to comfyflow api url
export COMFYFLOW_API_URL=http://38.207.176.168/
# set COMFYUI_SERVER_ADDR to comfyui server addr
export COMFYUI_SERVER_ADDR=/http://42.192.108.200:6889/
# set MODE to Creator
export MODE=Creator

# script params
python -m streamlit run Home.py
