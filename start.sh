#!/bin/bash
app="docker.test"
#docker build -t ${app} .
docker run -d -p 7000:80 \
  #--name=${app} \
  -v $PWD:/app ${app}

