#!/usr/bin/env bash

key="$1"

if [ "$key" == "all" ]; then
    cd src/
    make install
    make preprocess
    make generate
    make frontend
    cd ..
elif [ "$key" == "frontend" ]; then
    cd src/
    make frontend
    cd ..
elif [ "$key" == "preprocess" ]; then
    cd src/
    make preprocess
    cd ..
elif [ "$key" == "backend" ]; then
    cd src/
    make backend
    cd ..
elif [ "$key" == "install" ]; then
    cd src/
    make install
    cd ..
elif [ "$key" == "generate" ]; then
    cd src/
    python synthetic_download.py
    cd ..
elif [ "$key" == "detect" ]; then
    cd src/
    python detect.py
    cd ..
else
    echo "Unknown argument ${key}"
fi


