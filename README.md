# Image Compression with Recurrent Neural Network and Generalized Divisive Normalization



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
## Download Models
We provide pre-trained models on above datasets for architecture defined in paper: We will soon make more chnages in models and arhitecture. Watch out for changes to this repo. "Note", Image encoding and decoding utilizes GPU, if you have no GPU then please copy all data inside "results" folder. You can easily produce same results. 
[Pre-trained Models](https://drive.google.com/drive/u/1/folders/1M5df3rNMS1EIEfsvm1C7PitthNZA4Hmw)

## Testing on pre-trained models
Encode and decode with model
```bash
bash test/enc_dec.sh
```

## Citation
If you find this code useful for your research, please cite our work

```bash
@InProceedings{Islam_2021_CVPR,
    author    = {Islam, Khawar and Dang, L. Minh and Lee, Sujin and Moon, Hyeonjoon},
    title     = {Image Compression With Recurrent Neural Network and Generalized Divisive Normalization},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
    month     = {June},
    year      = {2021},
    pages     = {1875-1879}
}
```
## Contact
If you find any problem in code and want to ask any question, please send us email
khawar512@gmail.com, khawarislam@fuuast.edu.pk

## Acknowledgment
This implementation of code is heavily borrows from Biao Zhang
