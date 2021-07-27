#!/usr/bin/env bash

key="$1"
value="$2"

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
elif [ "$key" == "profile" ]; then
    cd src/
    if [ "$value" == "" ]; then
      echo "Unknown argument ${value}"
      exit 1
    fi
    python profiler.py -f "$value"
    cd ..
else
    cd src/
    make frontend
    cd ..
fi


