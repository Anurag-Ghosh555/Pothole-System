import cv2 as cv
import os

mode = input("Enter 'v' to record video or 'p' to take photos: ").strip().lower()

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")  
    exit()

if mode == 'v':
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    video_output = cv.VideoWriter('output_video.mp4', cv.VideoWriter_fourcc(*'mp4v'), 10, (width, height))
    print("Recording video... Press 'q' to stop.")
else:
    result_path = "photos"
    os.makedirs(result_path, exist_ok=True)
    print("Taking photos... Press '1' to take a photo and 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv.imshow('Webcam', frame)

    if mode == 'v':
        video_output.write(frame)

    if mode == 'p':
        key = cv.waitKey(1)
        if key == ord('1'):
            img_name = os.path.join(result_path, f"photo_{cv.getTickCount()}.jpg")
            cv.imwrite(img_name, frame)
            print(f"Saved {img_name}")
        elif key == ord('q'):
            break

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
if mode == 'v':
    video_output.release()
cv.destroyAllWindows()
