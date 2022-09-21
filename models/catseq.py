import torch
import torch.nn as nn


class CatSeq(nn.Module):
    def __init__(self, device, input_size, hidden_size, batch_size, drop_rate, vocab_size):
        super(CatSeq, self).__init__()
        self.device = device
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.batch_size = batch_size
        self.target_encoder = nn.GRU(bidirectional=False, input_size=input_size, hidden_size=hidden_size)
        self.encoder = nn.LSTM(bidirectional=True, input_size=input_size, hidden_size=hidden_size)
        self.decoder = nn.GRU(bidirectional=False, input_size=input_size, hidden_size=hidden_size)
        self.dropout = nn.Dropout(drop_rate)
        self.fc = nn.Linear(in_features=hidden_size, out_features=vocab_size)
        self.ln = nn.LayerNorm

    def forward(self, x, y):
        return

    def weight_init(self):
        for module in self.modules():
            if isinstance(module, nn.GRU):
                pass
            if isinstance(module, nn.LSTM):
                pass
            if isinstance(module, nn.Linear):
                nn.init.xavier_normal_(module.weight, gain=1)