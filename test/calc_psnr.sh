#!/bin/bash

BPG=test/psnr/bpg_psnr.csv
BPG420=test/psnr/bpg420_psnr.csv
LSTM=test/psnr/lstm_psnr.csv
GDN=test/psnr/gdn_psnr.csv
JPEG=test/psnr/jpeg_psnr.csv

echo -n "" > $BPG
for i in {01..24..1}; do
  echo Processing test/image_codec/bpg/kodim$i
  for j in {01..15..1}; do
    echo -n `python metric.py -m psnr -o test/images/kodim$i.png -c test/codec_images/bpg/kodim$i/$j.jpg`', ' >> $BPG
  done
  echo "" >> $BPG
done

echo -n "" > $BPG420
for i in {01..24..1}; do
  echo Processing test/bpg420/kodim$i
  for j in {01..15..1}; do
    echo -n `python metric.py -m psnr -o test/images/kodim$i.png -c test/codec_images/bpg420/kodim$i/$j.jpg`', ' >> $BPG420
  done
  echo "" >> $BPG420
done

echo -n "" > $LSTM
for i in {01..24..1}; do
  echo Processing test/codec_image/lstm/kodim$i
  for j in {01..15..1}; do
    echo -n `python metric.py -m psnr -o test/images/kodim$i.png -c test/codec_images/lstm/kodim$i/$j.png`', ' >> $LSTM
  done
  echo "" >> $LSTM
done

echo -n "" > $JPEG
for i in {01..24..1}; do
  echo Processing test/codec_image/jpeg/kodim$i
  for j in {01..15..1}; do
    echo -n `python metric.py -m psnr -o test/images/kodim$i.png -c test/codec_images/jpeg/kodim$i/$j.jpg`', ' >> $JPEG
  done
  echo "" >> $JPEG
done

echo -n "" > $GDN
for i in {01..24..1}; do
  echo Processing test/codec_image/jpegGDN/kodim$i
  for j in {01..15..1}; do
    echo -n `python metric.py -m psnr -o test/images/kodim$i.png -c test/codec_images/jpegGDN/kodim$i/$j.jpg`', ' >> $GDN
  done
  echo "" >> $GDN
done