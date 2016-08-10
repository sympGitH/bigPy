# coding: utf-8

import pandas as pd

def read_text(filename, sep=','):
    frame = pd.read_csv(filename, sep)
    # 열제목에 삽입될 수 있는 공백 제거 후, 열제목 교체
    frame.columns = [title.strip() for title in frame.columns]
    return frame