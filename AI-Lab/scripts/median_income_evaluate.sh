#!/bin/env bash

count=0

for i in {1..15}; do
  echo "For $i. we have:"
  cat ./output.txt | grep -F "$i." | wc -l
  echo ""
done
