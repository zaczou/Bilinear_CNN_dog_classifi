#!/usr/bin/evn python
# -*- coding: utf-8 -*-


import torch
from torch.autograd import Variable


model = torch.load('models/better1.pkl')
print model
for p in model.parameters():
    print p