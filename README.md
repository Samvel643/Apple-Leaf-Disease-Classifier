# Apple-Leaf-Disease-Classifier

Deep learning model for Apple Leaf Disease Classification (Plant Pathology 2021).

## Members
* Samvel Fahradyan
* Erik Bagdasaryan
* Anastasiya Tikunova
* Aram Khachatryan

## Project Overview
The goal of this project is to build a robust Computer Vision Deep Learning model to accurately classify apple leaf diseases based on the Plant Pathology 2021 - FGVC8 dataset. The model is designed to handle complex scenarios, including leaves with multiple concurrent diseases and varying background lighting conditions.

## Architecture & Techniques
* **Model Architecture:** We utilized a pre-trained **ResNet-50** architecture, modifying the final fully connected layer to output probabilities for our 6 target classes. Transfer learning was chosen to leverage robust feature extraction from ImageNet, speeding up convergence.
* **Data Splitting:** To handle multi-label dependencies effectively, we applied **Multi-label Iterative Stratification**.
* **Explainability:** We implemented **Grad-CAM** to visualize the specific regions of the leaf that trigger disease classifications, ensuring our model learns meaningful biological features rather than background noise.

## Results & Data Analysis

<img width="479" height="463" alt="Screenshot_7" src="https://github.com/user-attachments/assets/e66666a4-27cd-4bc8-a4ad-b33ccb1678a7" />



## How to Run

Instead of a command-line script, we have provided a clean, standalone inference notebook. Model weights are automatically downloaded from Google Drive, and the script applies the exact training transforms to output clear, human-readable predictions and heatmaps.

Test the model instantly by opening the predictor in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Samvel643/Apple-Leaf-Disease-Classifier/blob/main/predictor.ipynb)

**Steps:**
1. Click the **Open in Colab** badge above.
2. Run all cells sequentially (`Runtime` -> `Run all`).
3. In the final cell, you will be prompted to upload any raw `.jpg` leaf image. The script will decode the output and display the predicted disease, confidence score, and a Grad-CAM heatmap.
