# YOLOv8 Training with Optimized GPU Memory Usage

This repository contains code to train the YOLOv8 model with optimized GPU memory usage. The training script is designed to minimize GPU memory consumption by utilizing specific configurations and parameters.

## Prerequisites

- Python 3.8 or later
- Anaconda
- NVIDIA GPU with CUDA support
- PyTorch with CUDA

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/pamangie/yolov8training
cd yolov8-training-optimized

### 2. Create and Activate Anaconda Environment

conda create -n yolov8_env python=3.8
conda activate yolov8_env

### 3. Grant Access to the datasets Directory

Ensure that you have full access permissions for the datasets directory. Run the following command in the Command Prompt with administrator privileges:

```bash
icacls "C:\path\to\yolov8-training-optimized\datasets" /grant "%username%:F" /T

