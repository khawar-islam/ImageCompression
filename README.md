# Image compression with recurrent neural network and generalized divisive normalization



## Prerequisites
The implementation of out network is in Python 3.5.6 and PyTorch. We recommended using conda to install the dependencies. First, create a Python 3.5.6 environment. At this moment, my env name is "Fresh_RNN"

```bash
git clone https://github.com/khawar512/ImageCompression
cd ImageCompression
conda create -n Fresh_RNN python=3.5.6    
conda activate Fresh_RNN
```
pip users:

```bash
pip3 install -r requirements.txt
```

Then, install basic dependencies with conda or pip

## Requirements

```bash
numpy==1.15.2
matplotlib==3.0.0
scipy==1.1.0
torchvision==0.6.1
pillow==5.2.0
torch==1.5.1
```
If your machine has multiple GPUs, you can select which GPU you want to run on by setting the environment variable, 

```bash
CUDA_VISIBLE_DEVICES=0
```

## Data Preparation
We first need to prepare the training data. We take approximately 3700 images that generates 9 million patches. The data is from flicker.com. You can download data from and patch generation file from [Link](https://github.com/liujiaheng/CompressionData). Then generate the 32*32 patches using following script.

Testing has been done on popular Kodak Photo dataset
```bash
bash test/download_kodak.sh
```

## Training
Loading data takes time
```bash
python train.py -f /path/32x32_images
```

## Test
Encode and decode with model
```bash
bash test/enc_dec.sh
```

## Citation
If you find this code useful for your research, please cite our work

```bash
@inproceedings{wu2018vcii,
  title={Image compression with recurrent neural network and generalized divisive 
  normalization},
  author={Khawar Islam},
  booktitle={Under Review},
  year={2020}
}
```
## Acknowledgment
This implementation of code is heavily borrows from pytorch-image-comp-rnn by Biao Zhang
