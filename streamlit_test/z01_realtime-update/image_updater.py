""" 画像を生成して保存する工程を繰り返すプログラム
"""
from pathlib import Path
import time

import numpy as np
from PIL import Image

if __name__ == "__main__":
    colors = [
        (255, 255, 255),
        (0, 0, 0),
        (255, 0, 0), 
        (0, 255, 0), 
        (0, 0, 255), 
        (255, 255, 0), 
        (0, 255, 255), 
        (255, 0, 255), 
        (128, 0, 0), 
        (0, 128, 0), 
        (0, 0, 128), 
        (128, 128, 0), 
        (0, 128, 128), 
        (128, 0, 128), 
    ]

    file_dir = Path(__file__).absolute().parent
    root_dir = file_dir.parent.parent
    save_dir = root_dir.joinpath(f"results/{file_dir.stem}")
    save_dir.mkdir(parents=True, exist_ok=True)
    save_file = save_dir.joinpath("tmp_color.jpg")

    idx = 0
    while(True):
        try:
            color = colors[idx]
            idx+=1

            img = np.zeros((480, 640, 3), np.uint8)
            img[:, :,] = color

            pil_img = Image.fromarray(img)
            pil_img.save(save_file)
            print(f"Update {save_file} for {color}")

            if idx >= len(colors):
                idx = 0
            time.sleep(0.3)
        except KeyboardInterrupt:
            break