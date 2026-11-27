from ultralytics import YOLO
def main():
    model = YOLO("saved_models/yolo26l-cls-best.pt")  

    metrics = model.val(
        data="data/val",  
        imgsz=320,
        batch=64,
        device=0,  
        plots=True,
    )

    print(f"Top-1 Accuracy: {metrics.top1:.4f}")
    print(f"Top-5 Accuracy: {metrics.top5:.4f}")
    print("Metrics dict:", metrics.results_dict)
    print("Speed (ms/img):", metrics.speed)
if __name__ == '__main__':
    main()
