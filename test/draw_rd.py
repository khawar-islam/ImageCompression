

'''
import os

import numpy as np
from scipy.misc import imread
import matplotlib.pyplot as plt

line = True

lstm_ssim = np.genfromtxt('test/lstm_ssim.csv', delimiter=',')
lstm_ssim = lstm_ssim[:, :-1]
if line:
    lstm_ssim = np.mean(lstm_ssim, axis=0)
    lstm_bpp = np.arange(1, 17) / 192 * 24
    plt.plot(lstm_bpp, lstm_ssim, label='LSTM', marker='o')
else:
    lstm_bpp = np.stack([np.arange(1, 17) for _ in range(24)]) / 192 * 24
    plt.scatter(
        lstm_bpp.reshape(-1), lstm_ssim.reshape(-1), label='LSTM', marker='o')

jpeg_ssim = np.genfromtxt('test/jpeg_ssim.csv', delimiter=',')
jpeg_ssim = jpeg_ssim[:, :-1]
if line:
    jpeg_ssim = np.mean(jpeg_ssim, axis=0)

jpeg_bpp = np.array([
    os.path.getsize('test/jpeg/kodim{:02d}/{:02d}.jpg'.format(i, q)) * 8 /
    (imread('test/jpeg/kodim{:02d}/{:02d}.jpg'.format(i, q)).size // 3)
    for i in range(1, 25) for q in range(1, 21)
]).reshape(24, 20)

if line:
    jpeg_bpp = np.mean(jpeg_bpp, axis=0)
    plt.plot(jpeg_bpp, jpeg_ssim, label='JPEG', marker='x')
else:
    plt.scatter(
        jpeg_bpp.reshape(-1), jpeg_ssim.reshape(-1), label='JPEG', marker='x')


#BPG

bpg_ssim = np.genfromtxt('test/bpg_ssim.csv', delimiter=',')
bpg_ssim = bpg_ssim[:, :-1]
if line:
    bpg_ssim = np.mean(bpg_ssim, axis=0)

bpg_bpp = np.array([
    os.path.getsize('test/bpg/kodim{:02d}/{:02d}.jpg'.format(i, q)) * 8 /
    (imread('test/bpg/kodim{:02d}/{:02d}.jpg'.format(i, q)).size // 3)
    for i in range(1, 25) for q in range(1, 21)
]).reshape(24, 20)

if line:
    bpg_bpp = np.mean(bpg_bpp, axis=0)
    plt.plot(bpg_bpp, bpg_ssim, label='BPG', marker='x')
else:
    plt.scatter(
        bpg_bpp.reshape(-1), bpg_ssim.reshape(-1), label='BPG', marker='x')



#BPG 420

bpg_ssim_420 = np.genfromtxt('test/bpg_ssim.csv', delimiter=',')
bpg_ssim_420 = bpg_ssim_420[:, :-1]
if line:
    bpg_ssim_420 = np.mean(bpg_ssim_420, axis=0)

bpg_bpp420 = np.array([
    os.path.getsize('test/bpg420/kodim{:02d}/{:02d}.jpg'.format(i, q)) * 8 /
    (imread('test/bpg420/kodim{:02d}/{:02d}.jpg'.format(i, q)).size // 3)
    for i in range(1, 25) for q in range(1, 21)
]).reshape(24, 20)

if line:
    bpg_bpp420 = np.mean(bpg_bpp420, axis=0)
    plt.plot(bpg_bpp420, bpg_ssim_420, label='BPG420', marker='x')
else:
    plt.scatter(
        bpg_bpp420.reshape(-1), bpg_ssim_420.reshape(-1), label='BPG(4:2:0)', marker='*')


# Khawar
gdn_ssim = np.genfromtxt('test/GDN_ssim.csv', delimiter=',')
gdn_ssim = gdn_ssim[:, :-1]
if line:
    gdn_ssim = np.mean(gdn_ssim, axis=0)
    gdn_bpp = np.arange(1, 17) / 192 * 24
    plt.plot(gdn_bpp, gdn_ssim, label='Ours', marker='x')
else:
    gdn_bpp = np.stack([np.arange(1, 17) for _ in range(24)]) / 192 * 24
    plt.scatter(
        gdn_bpp.reshape(-1), gdn_ssim.reshape(-1), label='Ours', marker='x')


plt.xlim(0., 1.)
plt.xticks(np.arange(0, 1.1, .1))
plt.ylim(0.80, 1.0)
plt.xlabel('Bit Per Pixel (BPP)')
plt.ylabel('MS-SSIM (RGB)')
plt.legend()
plt.grid()
plt.savefig('GDNCNN.png')
plt.show()

'''

import os

import numpy as np
from scipy.misc import imread
import matplotlib.pyplot as plt

line = True

#=======================================================LSTM==============================================
lstm_ssim = np.genfromtxt('test/lstm_ssim.csv', delimiter=',')
lstm_ssim = lstm_ssim[:, :-1]
if line:
    lstm_ssim = np.mean(lstm_ssim, axis=0)
    lstm_bpp = np.arange(1, 17) / 192 * 24
    plt.plot(lstm_bpp, lstm_ssim, label='LSTM', marker='o')
else:
    lstm_bpp = np.stack([np.arange(1, 17) for _ in range(24)]) / 192 * 24
    plt.scatter(
        lstm_bpp.reshape(-1), lstm_ssim.reshape(-1), label='LSTM', marker='o')


#=======================================================Ours(GDN)==============================================
gdn_ssim = np.genfromtxt('test/gdn_ssim.csv', delimiter=',')
gdn_ssim = gdn_ssim[:, :-1]
if line:
    gdn_ssim = np.mean(gdn_ssim, axis=0)
    gdn_bpp = np.arange(1, 17) / 192 * 24
    plt.plot(gdn_bpp, gdn_ssim, label='Ours', marker='o')
else:
    gdn_bpp = np.stack([np.arange(1, 17) for _ in range(24)]) / 192 * 24
    plt.scatter(
        gdn_bpp.reshape(-1), gdn_ssim.reshape(-1), label='Ours', marker='o')

#=======================================================WebP==============================================
webP_ssim = np.genfromtxt('test/webP_ssim.csv', delimiter=',')
webP_ssim = webP_ssim[:, :-1]
if line:
    webP_ssim = np.mean(webP_ssim, axis=0)
    webP_bpp = np.arange(1, 17) / 192 * 24
    plt.plot(webP_bpp, webP_ssim, label='webP', marker='o')
else:
    webP_bpp = np.stack([np.arange(1, 17) for _ in range(24)]) / 192 * 24
    plt.scatter(
        webP_bpp.reshape(-1), webP_ssim.reshape(-1), label='webP', marker='o')

#=======================================================JPEG==============================================
jpeg_ssim = np.genfromtxt('test/jpeg_ssim.csv', delimiter=',')
jpeg_ssim = jpeg_ssim[:, :-1]
if line:
    jpeg_ssim = np.mean(jpeg_ssim, axis=0)

jpeg_bpp = np.array([
    os.path.getsize('test/jpeg/kodim{:02d}/{:02d}.jpg'.format(i, q)) * 8 /
    (imread('test/jpeg/kodim{:02d}/{:02d}.jpg'.format(i, q)).size // 3)
    for i in range(1, 25) for q in range(1, 21)
]).reshape(24, 20)

if line:
    jpeg_bpp = np.mean(jpeg_bpp, axis=0)
    plt.plot(jpeg_bpp, jpeg_ssim, label='JPEG', marker='x')
else:
    plt.scatter(
        jpeg_bpp.reshape(-1), jpeg_ssim.reshape(-1), label='JPEG', marker='x')






'''
plt.xlim(0., 2.)
plt.xticks(np.arange(0, 2.2, .2))
plt.ylim(0.80, 1.0)
plt.xlabel('Bit Per Pixel (BPP)')
plt.ylabel('MS-SSIM (RGB)')
plt.legend()
plt.grid()
plt.savefig('GDNCNN.png')
plt.show()
'''

plt.xlim(0., 1.)
plt.xticks(np.arange(0, 1.1, .1))
plt.ylim(0.80, 1.0)
plt.xlabel('Bit Per Pixel (BPP)')
plt.ylabel('MS-SSIM (RGB)')
plt.legend()
plt.grid()
plt.savefig('GDNCNN.png')
plt.show()
