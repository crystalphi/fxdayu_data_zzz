#! /bin/bash

source /etc/profile
export fxdayu=/fxdayu

dataz master update
dataz request tick
dataz master file
dataz write master
dataz master db
dataz freq update
dataz freq check
dataz write freq
dataz freq check
dataz idx
