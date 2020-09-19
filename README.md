# ImageCompression

Image Compression With Recurrent Neural Networks

Requirements
PyTorch 0.2.0
Train
python train.py -f /path/to/your/images/folder/like/mscoco

Encode and Decode
Encode
python encoder.py --model checkpoint/encoder_epoch_00000005.pth --input /path/to/your/example.png --cuda --output ex --iterations 16

This will output binary codes saved in .npz format.

Decode
python decoder.py --model checkpoint/encoder_epoch_00000005.pth --input /path/to/your/example.npz --cuda --output /path/to/output/folder

This will output images of different quality levels.

Test
Get Kodak dataset
bash test/get_kodak.sh
Encode and decode with RNN model
bash test/enc_dec.sh
Encode and decode with JPEG (use convert from ImageMagick)
bash test/jpeg.sh
Calculate SSIM
bash test/calc_ssim.sh
Draw rate-distortion curve
python test/draw_rd.py
Result
LSTM (Additive Reconstruction), before entropy coding

Rate-distortion