import torch.nn as nn
import torch.nn.functional as F

from modules import ConvLSTMCell, Sign, GDN


class EncoderCell(nn.Module):
    def __init__(self):
        super(EncoderCell, self).__init__()

        self.conv = nn.Conv2d(3, 64, kernel_size=3, stride=2, padding=1, bias=False)
        self.gdn1 = GDN(64)

        #self.conv2 = nn.Conv2d(3, 64, kernel_size=3, stride=2, padding=1, bias=False)
        #self.gdn2 = GDN(64)

        #self.relu = nn.LeakyReLU()

        self.rnn1 = ConvLSTMCell(
            64,
            256,
            kernel_size=3,
            stride=2,
            padding=1,
            hidden_kernel_size=1,
            bias=False)
        self.rnn2 = ConvLSTMCell(
            256,
            512,
            kernel_size=3,
            stride=2,
            padding=1,
            hidden_kernel_size=1,
            bias=False)
        self.rnn3 = ConvLSTMCell(
            512,
            512,
            kernel_size=3,
            stride=2,
            padding=1,
            hidden_kernel_size=1,
            bias=False)

    def forward(self, input, hidden1, hidden2, hidden3):
        # x = self.conv(input)
        # x = self.relu(self.gdn1(self.conv(input)))
        # x = self.gdn2(self.gdn1(self.conv(input)))
        # print(x)

        x = self.gdn1(self.conv(input))
        #x = self.gdn2(self.conv2(input))

        hidden1 = self.rnn1(x, hidden1)
        x = hidden1[0]

        hidden2 = self.rnn2(x, hidden2)
        x = hidden2[0]

        hidden3 = self.rnn3(x, hidden3)
        x = hidden3[0]

        return x, hidden1, hidden2, hidden3


class Binarizer(nn.Module):
    def __init__(self):
        super(Binarizer, self).__init__()
        self.conv = nn.Conv2d(512, 32, kernel_size=1, bias=False)
        self.sign = Sign()

    def forward(self, input):
        feat = self.conv(input)
        x = F.tanh(feat)
        return self.sign(x)


class DecoderCell(nn.Module):
    def __init__(self):
        super(DecoderCell, self).__init__()

        self.conv1 = nn.Conv2d(32, 512, kernel_size=1, stride=1, padding=0, bias=False)
        self.igdn1 = GDN(512, inverse=True)

       # self.conv3 = nn.Conv2d(32, 512, kernel_size=1, stride=1, padding=0, bias=False)
       # self.igdn3 = GDN(512, inverse=True)
        # self.reluDec = nn.LeakyReLU()

        self.rnn1 = ConvLSTMCell(
            512,
            512,
            kernel_size=3,
            stride=1,
            padding=1,
            hidden_kernel_size=1,
            bias=False)
        self.rnn2 = ConvLSTMCell(
            128,
            512,
            kernel_size=3,
            stride=1,
            padding=1,
            hidden_kernel_size=1,
            bias=False)
        self.rnn3 = ConvLSTMCell(
            128,
            256,
            kernel_size=3,
            stride=1,
            padding=1,
            hidden_kernel_size=3,
            bias=False)
        self.rnn4 = ConvLSTMCell(
            64,
            128,
            kernel_size=3,
            stride=1,
            padding=1,
            hidden_kernel_size=3,
            bias=False)
        self.conv2 = nn.Conv2d(32, 3, kernel_size=1, stride=1, padding=0, bias=False)

    def forward(self, input, hidden1, hidden2, hidden3, hidden4):
        # x = self.conv1(input)
        # x = self.reluDec(self.igdn1(self.conv1(input)))
        x = self.igdn1(self.conv1(input))
        #x = self.igdn3(self.conv3(input))

        hidden1 = self.rnn1(x, hidden1)
        x = hidden1[0]
        x = F.pixel_shuffle(x, 2)

        hidden2 = self.rnn2(x, hidden2)
        x = hidden2[0]
        x = F.pixel_shuffle(x, 2)

        hidden3 = self.rnn3(x, hidden3)
        x = hidden3[0]
        x = F.pixel_shuffle(x, 2)

        hidden4 = self.rnn4(x, hidden4)
        x = hidden4[0]
        x = F.pixel_shuffle(x, 2)

        x = F.tanh(self.conv2(x)) / 2

        return x, hidden1, hidden2, hidden3, hidden4
