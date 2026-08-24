import argparse
# import torch
# import torchvision.transforms as transforms
from PIL import Image

# [TODO: Import your model class here if it's in a separate file]
# from model import MyModel 

# Disease class names (adjust according to your dataset)
CLASS_NAMES = [
    "complex", "frog_eye_leaf_spot", "powdery_mildew", "rust", "scab", "healthy"
]

def load_model(weights_path):
    """Loads the trained model (saved weights) without retraining."""
    print(f"Loading model from {weights_path}...")
    
    # [TODO: Write your code to load the model]
    # model = MyModel(num_classes=len(CLASS_NAMES))
    # model.load_state_dict(torch.load(weights_path, map_location='cpu'))
    # model.eval() 
    
    # return model
    pass

def preprocess_image(image_path):
    """Applies the exact same preprocessing used during training."""
    try:
        image = Image.open(image_path).convert("RGB")
    except Exception as e:
        print(f"Error opening image: {e}")
        return None

    # [TODO: Apply your transforms (Resize, Normalize, ToTensor)]
    # transform = transforms.Compose([
    #     transforms.Resize((224, 224)),
    #     transforms.ToTensor(),
    #     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    # ])
    # tensor_image = transform(image).unsqueeze(0) # Add batch dimension
    # return tensor_image
    
    return image # Temporary, until the code above is uncommented

def predict(model, tensor_image):
    """Performs inference and prints human-readable results."""
    
    # [TODO: Pass the image through the model]
    # with torch.no_grad():
    #     outputs = model(tensor_image)
    #     # Since Plant Pathology can have multiple diseases at once,
    #     # you probably used Sigmoid (or Softmax if single-label):
    #     probabilities = torch.sigmoid(outputs).squeeze().numpy()
    
    # This is just temporary mock data to see how it works
    import numpy as np
    probabilities = np.array([0.05, 0.92, 0.01, 0.12, 0.88, 0.00]) 
    
    print("-" * 50)
    print("Results:")
    
    results = []
    for i, prob in enumerate(probabilities):
        if prob > 0.5: # Threshold to consider the disease present
            results.append(f"{CLASS_NAMES[i]} | Confidence: {prob * 100:.1f}%")
    
    if not results:
        print("No disease confidently detected (Possibly Healthy).")
    else:
        for res in results:
            print(f"-> Prediction: {res}")
    print("-" * 50)

if __name__ == "__main__":
    # Allows passing the image path from the terminal
    parser = argparse.ArgumentParser(description="Inference script for Apple Leaf Disease Classification")
    parser.add_argument("--image_path", type=str, required=True, help="Path to the raw image (e.g., leaf.jpg)")
    parser.add_argument("--weights_path", type=str, default="best_model.pth", help="Path to the saved model weights file")
    args = parser.parse_args()

    model = load_model(args.weights_path)
    tensor_image = preprocess_image(args.image_path)
    
    if tensor_image is not None:
        predict(model, tensor_image)
