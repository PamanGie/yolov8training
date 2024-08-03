import torch
from ultralytics import YOLO

def main():
    # Load YOLOv8 model
    model = YOLO('yolov8n.pt')  # Gunakan model YOLOv8 pre-trained

    # Path ke file konfigurasi data YAML
    data_config_path = 'C:/Users/your pc username/path/to/datasets/data.yaml'

    # Train model
    model.train(data=data_config_path, epochs=100, batch=16, imgsz=640, name='yolov8_coco')

    # Save trained model
    model.save('models/fire.pt')

if __name__ == '__main__':
    import multiprocessing as mp
    mp.freeze_support()  # Add this to use multiprocessing at Windows
    main()
