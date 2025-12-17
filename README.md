# 🧠 Brain Tumor Classification App  
A Streamlit-based machine learning application for classifying brain MRI images into **Glioma**, **Meningioma**, **Pituitary**, or **No Tumor** using texture‑based features (GLCM + LBP) and an SVM classifier.

---

## 📌 Overview  
This project provides a lightweight, fast, and educational tool for analyzing brain MRI images.  
The system extracts texture features from the uploaded image and predicts the tumor class using a trained machine learning model.

✅ Built for research and learning  
✅ Fully local processing  
✅ Clean UI with explanations and insights  

> ⚠️ **Disclaimer:** This application is not intended for medical diagnosis.  
> It is a research and educational tool only.

---

## 🖼️ Demonstration  
Below are example screenshots of the application in action.  
Replace the image paths with your own screenshots.

### ✅ Home Interface  
![Home Page](demo/home.png)

### ✅ Upload & Prediction  
![Prediction Page](demo/prediction1.png)
![Prediction Page](demo/prediction2.png)

### ✅ Video Demonstration

---

## 🧠 Supported Classes  

- 🔴 **Glioma**
- 🔵 **Meningioma**
- 🟡 **Pituitary**
- 🟢 **No Tumor** (Normal)

---

## 🏗️ Project Structure
```bash
BrainMRITumorClassification/
├── model/
│ └── model_bundle.pkl # Trained model and scaler
├── notebook/
│ └── ComputerVision_Project.ipynb # Notebook train and explore model
├── data/
│ └── README.md # About dataset
├── outputs/
│ ├── plots/
│ │ ├── CNN/ # CNN History Train Plot
│ │ └── YOLO/ # YOLO History Train Plot
│ └── models/
│   └── best.pt # Trained YOLOv8 Model
├── report/ # Report about the application
├── src/
│ ├── __init__.py # To ensure this is python package
│ ├── data_preprocess.py # Preprocess data scripts
│ ├── evaluate.py # Evaluation model scripts
│ ├── model.py # Model creation scripts
│ ├── train.py # Model trains scripts
│ └── main.py # The main entry point
├── requirements.txt # All Dependencies
├── README.md # Project Documentation
├── .gitignore # Ignored files
└── LICENSE
```

---

## 🔧 Installation  

### 1. Clone repository  
```bash
git clone https://github.com/yourusername/brain-tumor-classifier.git
cd brain-tumor-classifier
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the app
```bash
streamlit run BrainTumorClassificationApp.py
```

## 📊 Model Information
- Model: Support Vector Machine (SVM)
- Features:
- GLCM (contrast, energy, homogeneity, correlation)
- LBP histogram (uniform patterns)
- Input Size: 224×224 grayscale MRI
- Dataset: Public MRI dataset (e.g., Kaggle Brain Tumor MRI Dataset) (https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)
