from torchvision import transforms
from PIL import Image

def preprocess_image(image_path):
    image = Image.open(image_path)

    transformation = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456 , 0.406] , [0.229 , 0.224 , 0.225])
    ])

    input_tensor = transformation(image).unsqueeze(0)

    return input_tensor


def get_class_names():
    class_file = '/Users/sid/Documents/Projects/dognet/preprocessing/class_names.txt'

    with open(class_file , 'r') as f:
        class_names = [line.strip() for line in f.readlines()]
    
    return class_names