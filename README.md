![](https://img.shields.io/badge/Creater-TCT-FFFF00) ![](https://img.shields.io/badge/development-python-006400) ![](https://img.shields.io/badge/Version-3.11.11-blue)

# VideoToGif
VideoToGif/影像轉Gif圖檔

![image](https://github.com/user-attachments/assets/d28cd720-104a-44c9-a3b1-b0e3ac683288)

-------

# 1. Package Introduce

## 1-1. OpenCV (cv2)
（Open Source Computer Vision Library）是一個開源的計算機視覺和機器學習軟件庫，旨在提供各種視覺任務的高效解決方案。它被廣泛應用於影像處理、物體檢測、影像分類、面部識別、計算機視覺等領域。

## 1-2. imageio
imageio 專門用於讀取和寫入多種影像與視頻格式。它的主要用途是提供一個簡單且一致的 API，方便開發者處理圖像、視頻和動畫等視覺內容。

### 主要功能：
- 支援多種影像格式： imageio 支援讀取和寫入各種常見的影像格式，如 PNG、JPEG、TIFF、GIF 等。它讓開發者不需要依賴不同的庫來處理不同的格式，從而簡化了影像處理的流程。

- 動態影像（GIF）處理： 其中一個強大的功能是支持 GIF 動畫的讀取、編輯和創建。開發者可以輕鬆地讀取 GIF 幀，編輯幀，或者將多張圖片合成為一個 GIF 動畫，這在創建動態內容時非常有用。

- 視頻處理： imageio 也支援視頻格式的處理，開發者可以輕鬆讀取和寫入視頻文件，如 MP4、AVI、MOV 等。這對於開發多媒體應用或處理視頻流的場景非常方便。

- 跨平台支持： imageio 是跨平台的，無論在 Windows、macOS 還是 Linux 上，都能順利運行，並且它支持多種後端處理庫（例如，FFmpeg 用於視頻處理），因此可以在不同的環境下處理各種影像與視頻格式。

- 簡化影像處理流程： 它提供的 API 使得影像讀寫變得直觀，開發者可以輕鬆地進行批次處理或流式處理，並且不需要手動處理影像格式的細節。

- 開發友好： 由於 imageio 的接口簡單直觀，即使是新手開發者也能快速上手，並將其整合到自己的項目中，無需花費過多時間在理解複雜的影像處理邏輯上。

- 擴展性： 除了常見的圖像格式外，imageio 還支援一些特殊格式的處理，如 HDF5、DICOM 和 FITS，這些格式在科學研究、醫學影像處理等領域中常見。
 
---

## 2. Install Command：
Please refer the command as below.

## 2-1. opencv 
```bash
pip install opencv-python imageio
```

## 2-2. imageio 
```bash
pip install imageio
```

------

## 3. py Code：

## 3-1. 01_VideoToGif.py

### 主要功能：
將指定的影像匯入並轉Gif

## 3-2. 02_CompressedGif_ReduceResolution.py

### 主要功能：
降低 GIF 解析度,透過 resize() 縮小圖片尺寸，減少 GIF 檔案大小。適用於 檔案過大但不要求高解析度 的情境。

## 3-3. 02_CompressedGif_ReduceFPS.py

### 主要功能：
降低 GIF 幀數 (FPS),刪減影格數量 (例如 30 FPS 降為 15 FPS) 來減少 GIF 檔案大小。適用於 動作變化不快的 GIF。

## 3-4. 02_CompressedGif_ReduceColor.py

### 主要功能：
減少顏色數量,GIF 最多支援 256 種顏色，降低顏色數量可以縮小檔案大小。適用於 單一色調 GIF 或對顏色需求不高的場合。

------

## 4. Result：

1.將影像轉Git圖片檔案

   01_VideoToGif.py


2.將原本的Git檔案大小再壓低

  - 02_CompressedGif_ReduceResolution.py
   
  - 02_CompressedGif_ReduceFPS.py
   
  - 02_CompressedGif_ReduceColor.py

   Before:
   
   25,756 KB
   (4秒車流影片)


   After:
   
  - 02_CompressedGif_ReduceResolution.py >  7,772  KB
   
  - 02_CompressedGif_ReduceFPS.py        > 12,993  KB
   
  - 02_CompressedGif_ReduceColor.py      > 20,042  KB

------

## About Me
Thanks & Best Regards !

蔡承廷

​Senior Engineer of Semiconductor Product/Testing & ​Automation

Email: ​​kp924606@gmail.com

LinkedIn:https://www.linkedin.comin/tsai-cheng-ting/



