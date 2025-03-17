#降低 GIF 幀數 (FPS)
#刪減影格數量 (例如 30 FPS 降為 15 FPS) 來減少 GIF 檔案大小。
#適用於 動作變化不快的 GIF。

import imageio

# 讀取 GIF
input_gif = "Data\output.gif"
output_gif = "Data\output_ReduceFPS.gif"

frames = imageio.mimread(input_gif)
new_frames = frames[::2]  # 每 2 張取 1 張 (FPS 降 50%)

# 儲存壓縮後的 GIF
imageio.mimsave(output_gif, new_frames, fps=15, loop=0)  # 設定較低 FPS
print(f"降低 FPS 的 GIF 已儲存: {output_gif}")