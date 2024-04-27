import torch
import torch.nn as nn
from torchvision import models


def load_model():
    state_dict_path = '/Users/sid/Documents/Projects/dognet/model_state_dict.pth'
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = models.resnet50()
    num_ftrs = model.fc.in_features
    model.fc = nn.Sequential(
                            nn.Linear(num_ftrs , 1000),
                            nn.ReLU(),
                            nn.Dropout(p=0.3),
                            nn.Linear(1000 , 120)
                        )
    model.load_state_dict(torch.load(state_dict_path , map_location=device))
    model.eval()
    return model

