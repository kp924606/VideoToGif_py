#Version=3.11.11

#1.安裝 opencv
#pip install opencv-python imageio

#2.安裝 imageio
#pip install imageio

import cv2
import time
import imageio
import sys

from ultralytics import YOLO

cv2.namedWindow('YOLOv8', cv2.WINDOW_NORMAL)

# 影像來源
target = fr"D:\Video\Traffic_01.mp4"

# 載入 YOLOv8 模型
model = YOLO('yolov8x.pt')

# 開啟影像
cap = cv2.VideoCapture(target)

# 獲取影片總長度
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 影片總幀數
fps = cap.get(cv2.CAP_PROP_FPS)  # 影片的FPS
video_length = total_frames / fps  # 影片總時長，單位為秒

print(f"影片長度: {video_length}秒")

# 設定要抓取的時間區間（例如從第3秒到第7秒）
start_time = 2  # 開始時間（秒）
end_time = 6    # 結束時間（秒）

if start_time <0 or start_time > video_length :
    print(f"指定開始時間不符合影片長度或數值<0")
    sys.exit()  # 結束程式

if end_time < start_time or end_time > video_length :
    print(f"指定結束時間不符合影片長度或小時開始時間")
    sys.exit()  # 結束程式

# 計算開始與結束的幀數
start_frame = int(start_time * fps)
end_frame = int(end_time * fps)

fps = 30  # 設定目標 FPS (每秒 30 張影像)
frames = []  # 存放影格

# 將影片移動到起始幀位置
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)


while True:
    current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))  # 當前幀數
    
    # 當前幀大於結束幀數時，停止抓取
    if current_frame > end_frame:
        print("指定時間到，關閉...")    
        break

    r, frame = cap.read()
    
    if not r:
        print("無法讀取影像，關閉...")
        break

    # 用 YOLOv8 模型處理影像
    results = model(frame, verbose=False)
    frame = results[0].plot()

    # 儲存影格 (轉為 RGB，因為 OpenCV 預設是 BGR)
    frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

     # 顯示 FPS
    et = time.time()
    FPS = int(1 / (et - start_time))  # 計算 FPS
    cv2.putText(frame, 'FPS=' + str(FPS), (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2)
    cv2.imshow('YOLOv8', frame)

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
