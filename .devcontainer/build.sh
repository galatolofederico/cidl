#!/bin/sh

docker build . -t galatolofederico/cidl:latest -t galatolofederico/cidl:$(date +"%Y%m%d")
