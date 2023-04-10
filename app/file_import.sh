#!/bin/bash

foldername=$1
current_date=$(date +%m%d%Y_%H%M)

# Add date and time stamp to folder name
foldername="$foldername"_"$current_date"

folder_path="/code/$foldername"
grep_file="/code/$foldername/dict"
results_file="/code/$foldername/grep_results.txt"

# check if folder exists
if [ ! -d "$folder_path" ]; then
  echo "Folder not found: $foldername"
  exit 1
fi

# check if dict file exists
if [ ! -f "$grep_file" ]; then
  echo "Dict file not found: $grep_file"
  exit 1
fi

# create grep_results file if not exists
touch $results_file

# loop through each line of dict file and grep each file in folder for the line
while IFS= read -r line; do
  for file in $folder_path/*; do
    if [ -f "$file" ]; then
      grep -Hn "$line" "$file" >> "$results_file"
    fi
  done
done < "$grep_file"

# check if there are any results
if [ ! -s "$results_file" ]; then
  echo "No results found"
  exit 1
fi

echo "Results saved to $results_file"
