from pathlib import Path
import time

""" browze.py の画像2枚バージョン
"""
import streamlit as st
import numpy as np
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

if __name__ == "__main__":
    st.markdown("# Apprication ")
    empty1 = st.empty()
    empty2 = st.empty()

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
            empty1.image(img)

            img2 = img.transpose((1, 0, 2))
            empty2.image(img2)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(e)
            break


