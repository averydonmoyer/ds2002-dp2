#!/bin/bash

for file in data/*
do
  echo "Importing $file"
  /usr/bin/mongoimport --uri $MONGODB --collection test $file --jsonArray
done

