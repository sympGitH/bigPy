import sys

def hello(누구):
    인사말 = '안녕하세요. {0} 님!'.format(누구)
    return 인사말

def thanks(누구):
    감사말 = '감사합니다. {0} 님!'.format(누구)
    return 감사말

if __name__ == '__main__':
    print(sys.argv)
    인자=sys.argv[1:]
    
    for 이름 in 인자:
        print(thanks(이름))