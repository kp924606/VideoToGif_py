#減少顏色數量
#GIF 最多支援 256 種顏色，降低顏色數量可以縮小檔案大小。
#適用於 單一色調 GIF 或對顏色需求不高的場合。

import imageio
from PIL import Image

# 讀取 GIF
input_gif = "Data\output.gif"
output_gif = "Data\output_ReduceColor.gif"

frames = imageio.mimread(input_gif)

# 降低顏色數量 (轉為 128 色)
new_frames = [Image.fromarray(frame).convert("P", palette=Image.ADAPTIVE, colors=128) for frame in frames]

# 儲存壓縮後的 GIF
new_frames[0].save(output_gif, save_all=True, append_images=new_frames[1:], loop=0, optimize=True)
print(f"減少顏色數的 GIF 已儲存: {output_gif}")
