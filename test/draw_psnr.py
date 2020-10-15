import os

import numpy as np
from scipy.misc import imread
import matplotlib.pyplot as plt

line = True


lstm_ssim = np.genfromtxt("/home/khawar/Desktop/RNN_Fresh/pytorch-image-comp-rnn/test/jpeg_psnr.csv", delimiter=",")
lstm_ssim = lstm_ssim[:, :-1]
lstm_bpp = np.arange(1, lstm_ssim.shape[-1]+1) / 192 * 24
print(lstm_ssim.shape, lstm_bpp.shape)
lstm_ssim = lstm_ssim.mean(axis=0)
plt.plot(lstm_bpp, lstm_ssim, label="JPEG", marker='o')


bpg_psnr = np.genfromtxt("/home/khawar/Desktop/RNN_Fresh/pytorch-image-comp-rnn/test/lstm_psnr.csv", delimiter=",")
bpg_psnr = bpg_psnr[:, :-1]
bpg_bpp = np.arange(1, bpg_psnr.shape[-1]+1) / 192 * 24
print(bpg_psnr.shape, bpg_bpp.shape)
bpg_psnr = bpg_psnr.mean(axis=0)
plt.plot(bpg_bpp, bpg_psnr, label="LSTM", marker='o')


gdn_psnr = np.genfromtxt("/home/khawar/Desktop/RNN_Fresh/pytorch-image-comp-rnn/test/gdn_psnr.csv", delimiter=",")
gdn_psnr = gdn_psnr[:, :-1]
gdn_bpp = np.arange(1, gdn_psnr.shape[-1]+1) / 192 * 24
print(gdn_psnr.shape, gdn_bpp.shape)
gdn_psnr = gdn_psnr.mean(axis=0)
plt.plot(gdn_bpp, gdn_psnr, label="Ours", marker='o')

webP_psnr = np.genfromtxt("/home/khawar/Desktop/RNN_Fresh/pytorch-image-comp-rnn/test/webP_psnr.csv", delimiter=",")
webP_psnr = webP_psnr[:, :-1]
webP_bpp = np.arange(1, webP_psnr.shape[-1]+1) / 192 * 24
print(webP_psnr.shape, webP_bpp.shape)
webP_psnr = webP_psnr.mean(axis=0)
plt.plot(webP_bpp, webP_psnr, label="WebP", marker='o')
''''
gdn_psnr = np.genfromtxt("/home/khawar/Desktop/RNN_Fresh/pytorch-image-comp-rnn/test/psnr/GDN_psnr.csv", delimiter=",")

gdn_psnr = gdn_psnr[:, :-1]
gdn_bpp = np.arange(1, gdn_psnr.shape[-1]+1) / 192 * 24
print(gdn_psnr.shape, gdn_bpp.shape)
gdn_psnr = gdn_psnr.mean(axis=0)
plt.plot(gdn_bpp, gdn_psnr, label="Ours", marker='o')


plt.xlim(0, 1)
plt.xticks(np.arange(0, 1.1, .1))
plt.ylim(23, 32)
plt.xlabel('Bit Per Pixel (BPP)')
plt.ylabel('PSNR (RGB)')
plt.legend()
plt.show()
'''
'''
plt.xlim(0., 1.)
plt.xticks(np.arange(0, 2.2, .2))
plt.ylim(23, 38)
plt.xlabel('Bit Per Pixel (BPP)')
plt.ylabel('PSNR (RGB)')
plt.legend()
plt.grid()
plt.savefig('PSNR.png')
plt.show()
'''

plt.xlim(0., 1.)
plt.xticks(np.arange(0, 1.1, .1))
plt.ylim(23, 33)
plt.xlabel('Bit Per Pixel (BPP)')
plt.ylabel('PSNR (RGB)')
plt.legend()
plt.grid()
plt.savefig('PSNR.png')
plt.show()
