#!/bin/sh

# Commands to run the exiftool and export the metadata to csv

pwd

foldername=$1
timestamp=$2

echo "The folder is called $foldername"

results_file="/code/${foldername}_${timestamp}/metadata.csv"

cd "/code/${foldername}_${timestamp}"

exiftool -csv -r -All . >> "$results_file"

echo "Metadata output saved to $results_file"
