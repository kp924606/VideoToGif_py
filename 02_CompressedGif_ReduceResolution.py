#降低 GIF 解析度
#透過 resize() 縮小圖片尺寸，減少 GIF 檔案大小。
#適用於 檔案過大但不要求高解析度 的情境。

import imageio
from PIL import Image

# 讀取 GIF
input_gif = "Data\output.gif"
output_gif = "Data\output_compressed.gif"

# 讀取 GIF 影格
frames = imageio.mimread(input_gif)

# 設定縮小比例 (例如 50%)
scale = 0.5
new_frames = []
for frame in frames:
    img = Image.fromarray(frame)
    img = img.resize((int(img.width * scale), int(img.height * scale)), Image.Resampling.LANCZOS)
    new_frames.append(img)

# 儲存壓縮後的 GIF
new_frames[0].save(output_gif, save_all=True, append_images=new_frames[1:], loop=0, optimize=True)
print(f"壓縮後的 GIF 已儲存: {output_gif}")