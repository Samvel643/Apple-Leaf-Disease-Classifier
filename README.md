# Apple-Leaf-Disease-Classifier
Deep learning model for Apple Leaf Disease Classification (Plant Pathology 2021).

## Members
* Erik Bagdasaryan
* Samvel Fahradyan
* Anastasiya Tikunova
* Aram Khachatryan

## Project Overview
The goal of this project is to build a robust Computer Vision Deep Learning model to accurately classify apple leaf diseases based on the [Plant Pathology 2021 - FGVC8](https://www.kaggle.com/c/plant-pathology-2021-fgvc8) dataset. The model is designed to handle complex scenarios, including leaves with multiple concurrent diseases and varying background lighting conditions.

## Architecture
[TODO: Specify your final model architecture (e.g., ResNet50, EfficientNet). Mention if you used Transfer Learning and explain why you chose this specific architecture.]

## Results & Error Analysis
[TODO: Insert 1-2 visual graphs here, such as a Loss/Accuracy curve or a Confusion Matrix. 
Crucially, include 2-3 examples of incorrect predictions and explain why the neural network got confused, demonstrating a deep understanding of the dataset.]

## How to Run
1. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the `predict.py` script to make an inference on a new raw image:
   ```bash
   python predict.py --image_path path/to/leaf.jpg
