""" 画像ファイルを都度ロードして動的にブラウザ上に表示する。
"""
import time
from pathlib import Path

import streamlit as st
import numpy as np
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

if __name__ == "__main__":
    st.markdown("# Apprication ")

    image_loc = st.empty()

    file_dir = Path(__file__).absolute().parent
    root_dir = file_dir.parent.parent
    save_dir = root_dir.joinpath(f"results/{file_dir.stem}")
    save_dir.mkdir(parents=True, exist_ok=True)
    save_file = save_dir.joinpath("tmp_color.jpg")
    print(f"load file is {save_file}")

    while(True):
        try:
            try:
                pil_img = Image.open(save_file)
            except Exception as e:
                time.sleep(0.05)
                continue
            img = np.asanyarray(pil_img)
            image_loc.image(img)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(e)
            break