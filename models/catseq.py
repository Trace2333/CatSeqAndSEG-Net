import torch
import torch.nn as nn


class CatSeq(nn.Module):
    def __init__(self, device, input_size, hidden_size, batch_size):
        super(CatSeq, self).__init__()
        self.device = device
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.batch_size = batch_size