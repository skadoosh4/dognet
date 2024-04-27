import torch
import numpy as np
from PIL import Image
import torch.nn.functional as F
from preprocessing.image_utils import preprocess_image , get_class_names

def predict_image(image_path , model):
    input_tensor = preprocess_image(image_path)
    with torch.no_grad():
        output = model(input_tensor)
    probabilities = F.softmax(output , dim=1)

    top3_probs , top3_indices = torch.topk(probabilities , k=3 , dim=1)
    class_names = get_class_names()
    top3_classes = [class_names[idx.item()] for idx in top3_indices[0]]
    top3_probabilities = [prob.item() for prob in top3_probs[0]]

    top3_predictions = {
        top3_classes[i] : top3_probabilities[i] for i in range(len(top3_classes))
    }

    return top3_predictions
