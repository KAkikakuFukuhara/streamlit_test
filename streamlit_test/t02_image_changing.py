import streamlit as st
import numpy as np
import time

if __name__ == "__main__":
    st.markdown("# Application")
    image_loc = st.empty()

    canvas = np.zeros((480, 640, 3), dtype=np.uint8)

    colors = [
        [255, 0, 0],
        [0, 255, 0],
        [0, 0, 255],
        [255, 255, 0],
        [0, 255, 255],
        [255, 0, 255],
        [0, 0, 0]
    ]

    ci = 0
    while(True):
        try:
            time.sleep(1)
            canvas2 = canvas.copy()
            canvas2[:, :] = colors[ci]
            image_loc.image(canvas2)
            ci += 1
            if ci > len(colors)-1:
                ci = 0
        except KeyboardInterrupt:
            break
        except Exception:
            break
