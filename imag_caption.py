import gradio as gr
from PIL import Image
import torch
from torchvision import transforms
from model import ImageCaptioningModel  # Import your pre-trained image captioning model

# Function to preprocess the input image
def preprocess_image(image):
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    return preprocess(image).unsqueeze(0)

# Load your pre-trained image captioning model
model = ImageCaptioningModel()
model.load_state_dict(torch.load('C:/Users/Daveee/Downloads/weights_model.h5'))
model.eval()

# Function to generate caption for the input image
def generate_caption(input_image):
    # Preprocess the input image
    image = Image.fromarray(input_image.astype('uint8'), 'RGB')
    input_tensor = preprocess_image(image)

    # Generate caption using the pre-trained model
    caption = model.generate_caption(input_tensor)

    return caption

# Create a Gradio interface
gr.Interface(
    generate_caption, 
    gr.inputs.Image(type="pil"),  # Use "pil" type to accept PIL images
    "text",  # Output will be text (caption)
    title="Image Caption Generator",
    description="Upload an image and get its caption."
).launch()
