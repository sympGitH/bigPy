import pandas as pd

def importNC(데이터폴더):
    #경로='./data/NC Dinos {}.xlsx'
    경로=데이터폴더 + 'NC Dinos {}.xlsx'
    프레임목록 = []
    for 연도 in range(2013, 2016):
        프레임=pd.read_excel(경로.format(연도))
        프레임['시즌'] = 연도
        프레임=프레임.set_index('선수명')
        프레임목록.append(프레임)
        
    return 프레임목록


def findComLine(파일명, 시작패턴, encoding='utf-8'):
    주석줄번호목록 = []
    #텍스트 파일 열기
    파일=open(파일명, encoding=encoding)
    for 줄번호, 줄 in enumerate(파일):
        #현재 줄이 시작패턴에 부합하는지 확인
        if 줄.startswith(시작패턴):
            주석줄번호목록.append(줄번호)
    return 주석줄번호목록