#!/usr/bin/env bash
# install requirements
python3 -m pip install -r requirements.txt

# download spacy models
python3 -m spacy download en_core_web_md
python3 -m spacy download en_core_web_sm
python3 -m spacy download en_core_web_trf

