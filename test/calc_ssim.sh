#!/bin/bash

webP=test/webP_psnr.csv
#JPEG=test/jpeg_psnr.csv

echo -n "" > $webP
for i in {01..24..1}; do
  echo Processing test/webP/kodim$i
  for j in {00..15..1}; do
    echo -n `python metric.py -m psnr -o test/images/kodim$i.png -c test/webP/kodim$i/$j.webp`', ' >> $webP
  done
  echo "" >> $webP
done

#echo -n "" > $JPEG
#for i in {01..24..1}; do
#  echo Processing test/jpeg/kodim$i
#  for j in {01..20..1}; do
#    echo -n `python metric.py -m psnr -o test/images/kodim$i.png -c test/jpeg/kodim$i/$j.jpg`', ' >> $JPEG
#  done
#  echo "" >> $JPEG
#done
