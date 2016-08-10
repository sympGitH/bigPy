import pandas as pd
import sys, os

def importGrid(프레임, 표범위):
    표사전 = {}

    for 표정보 in 표범위:
        표제목, 시작, 종료 = 표정보
        표 = 프레임.iloc[시작:종료]
        표사전[표제목]=표
        
    return 표사전

def searchGrid(프레임):
    표제목행여부=프레임.notnull().sum(axis=1) == 1
    # 표제목 행은 값이 딱 하나만 담겨있다.
    표시작시리즈=pd.Series(프레임[표제목행여부].index)
    표길이=len(프레임)
    끝범위목록 = list(표시작시리즈[1:])
    끝범위목록.append(표길이)
    끝범위시리즈=pd.Series(끝범위목록)
    
    표제목 = [프레임.ix[i, 0] for i in 표시작시리즈]
    표범위 = list(zip(표제목, 표시작시리즈, 끝범위시리즈))
    
    return 표범위

def readExcel(경로):
    프레임=pd.read_excel(경로, skiprows=3, parse_cols='C:K', header=None)
    프레임=프레임.dropna(how='all')
    프레임=프레임.reset_index(drop=True)
    
    return 프레임

if __name__ == '__main__':
    인자=sys.argv[1:]
    
    #디렉토리인지 확인하는 작업 필요
    파일목록 = []
    for 항목 in 인자:
        if os.path.isdir(항목):
            파일목록.extend(os.listdir(항목))
        else:
            파일목록.append(항목)
    
    print ('처리 대상 파일목록')
    for 경로 in 파일목록:
        print (경로)
