# YOLOv8 Training Code

This repository contains code to train the YOLOv8 model with alternate way. 

## Prerequisites

- Python 3.8 or later
- Anaconda
- NVIDIA GPU with CUDA support
- PyTorch with CUDA

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/pamangie/yolov8training
cd yolov8training
```

### 2. Grant Access to the datasets Directory
```bash
# Run your command prompt as administrator and run this script below:
icacls "C:\path\to\yolov8training\datasets" /grant "%username%:F" /T
```

### 3. Train Your Model

```bash
Train the YOLOv8 Model
python train.py
```




