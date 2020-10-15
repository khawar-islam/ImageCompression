#!/bin/bash


#for i in {01..24..1}; do
#  echo JPEG Encoding test/images/kodim$i.png
#  mkdir -p test/jpeg/kodim$i
#  for j in {1..20..1}; do
#    convert test/images/kodim$i.png -quality $(($j*5)) -sampling-factor 4:2:0 test/jpeg/kodim$i/`printf "%02d" $j`.jpg
#  done
#done



#for i in {01..24..1}; do
#  echo WebP Encoding test/images/kodim$i.png
#  mkdir -p test/webP/kodim$i
#  for j in {0..20..1}; do
#    cwebp test/images/kodim$i.png -q $(($j*5)) -o test/webP/kodim$i/`printf "%02d" $j`.webp
#  done
#done


for i in {01..24..1}; do
  echo JP2 Encoding test/images/kodim$i.png
  mkdir -p test/JP2/kodim$i
  for j in {0..20..1}; do
    convert test/images/kodim$i.png -quality $(($j*5)) -colorspace YUV -sampling-factor 4,2 test/JP2/kodim$i/`printf "%02d" $j`.jp2
  done
done