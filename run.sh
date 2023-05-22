#!/usr/bin/env bash

# create virtual environment called text_classification
python3 -m venv linguistics_env

# activate virtual environment
source ./txt_classification_env/bin/activate

# install requirements
echo "[INFO] Installing requirements..."
python3 -m pip install -r requirements.txt

# download spacy model
echo "[INFO] Downloading spacy models..."
python3 -m spacy download en_core_web_md

# run analysis
echo "[INFO] Running analysis..."
python3 src/main.py

# deactivate virtual environment
echo "[INFO] Run Complete! Deactivating virtual environment..."
deactivate txt_classification_env