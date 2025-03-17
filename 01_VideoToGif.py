#Version=3.11.11

#1.安裝 opencv
#pip install opencv-python imageio

#2.安裝 imageio
#pip install imageio

import cv2
import time
import imageio

from ultralytics import YOLO

cv2.namedWindow('YOLOv8', cv2.WINDOW_NORMAL)

# 影像來源
target = fr"D:\Video\Traffic_01.mp4"

# 載入 YOLOv8 模型
model = YOLO('yolov8x.pt')

# 開啟影像
cap = cv2.VideoCapture(target)

frames = []  # 存放影格
start_time = time.time()  # 記錄開始時間
duration = 8  # 預設要抓的秒數(數值/2 大概就是要的秒數),注意影像本身的秒數也要確認
fps = 30  # 設定目標 FPS (每秒 30 張影像)

while True:
    st = time.time()
    r, frame = cap.read()
    
    if not r:
        print("無法讀取影像，關閉...")        
        break

    results = model(frame, verbose=False)
    frame = results[0].plot()

    et = time.time()
    FPS = int(1 / (et - st))  # 計算 FPS
    
    cv2.putText(frame, 'FPS=' + str(FPS), (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2)
    cv2.imshow('YOLOv8', frame)

    # 儲存影格 (轉為 RGB，因為 OpenCV 預設是 BGR)
    frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # 檢查時間，是否達到指定時間
    if time.time() - start_time > duration:
        break

    key = cv2.waitKey(1)  # 1ms 等待時間
    if key == 27:  # 按 ESC 退出
        break

cap.release()
cv2.destroyAllWindows()
print(f"Video 播放完畢, 正在儲存中...")

# 儲存 GIF
gif_filename = "Data\output.gif"
imageio.mimsave(gif_filename, frames, fps=fps)
print(f"GIF 已儲存: {gif_filename}")
