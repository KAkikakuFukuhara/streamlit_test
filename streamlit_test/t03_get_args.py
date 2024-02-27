""" 実行に引数を渡せるかの確認
"""
from argparse import ArgumentParser

import streamlit as st
import time

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("text", type=str, help="text")
    parser.add_argument("--text2", type=str, default="text2", help="text")
    cli_args = vars(parser.parse_args())
    # 数回呼ばれる。観察したところクライアントがアクセスするたびに呼ばれているようだ。
    print(cli_args["text"])
    print(cli_args["text2"])

    st.text("Application")

    while(True):
        try:
            time.sleep(0.5)
        except KeyboardInterrupt:
            print("break")
            break

    print("finish")