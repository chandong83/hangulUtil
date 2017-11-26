#-*- coding:utf-8 -*-
import sys
import re
# 만 단위 자릿수
tenThousandPos = 4
# 억 단위 자릿수
hundredMillionPos = 9
txtDigit = ['', '십', '백', '천', '만', '억']
txtNumber = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
txtPoint = '쩜 '

def isHangul(text):
    #Check the Python Version
    pyVer3 =  sys.version_info >= (3, 0)

    if pyVer3 : # for Ver 3 or later
        encText = text
    else: # for Ver 2.x
        if type(text) is not unicode:
            encText = text.decode('utf-8')
        else:
            encText = text

    hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', encText))
    return hanCount > 0


def digit2txt(strNum):
    resultStr = ''
    digitCount = 0
    #print(strNum)

    #자릿수 카운트
    for ch in strNum:
        if ch == '-':
            continue
        # ',' 무시
        elif ch == ',':
            continue
        #소숫점 까지
        elif ch == '.':
            break
        digitCount = digitCount + 1

    #수숫점 이하 확인하기
    ptExistFg = False
    #ptCheckFg = False

    ptValue = (float(strNum)%1)
    if ptValue > 0:
        ptExistFg = True
    '''
    for ch in strNum:
        #소숫점 까지
        if ch == '.':
            ptCheckFg = True
        elif ptCheckFg:
            if ch != '0':
                ptExistFg = True
                print(ch)
                break;
    '''

    digitCount = digitCount-1
    index = 0

    while True:
        notShowDigit = False
        ch = strNum[index]
        if ch == '-':
            index = index + 1
            if index >= len(strNum):
                break;
            continue
        #print(str(index) + ' ' + ch + ' ' +str(digitCount))
        # ',' 무시
        if ch == ',':
            index = index + 1
            if index >= len(strNum):
                break;
            continue

        if ch == '.':
            if ptExistFg == False:
                break;
            resultStr = resultStr + txtPoint
        else:
            #자릿수가 2자리이고 1이면 '일'은 표시 안함.
            # 단 '만' '억'에서는 표시 함
            if(digitCount > 0) and (digitCount != tenThousandPos) and  (digitCount != hundredMillionPos) and int(ch) == 1:
                resultStr = resultStr + ''
            elif int(ch) == 0:
                resultStr = resultStr + ''
                # 단 '만' '억'에서는 표시 함
                if (digitCount != tenThousandPos) and  (digitCount != hundredMillionPos):
                    notShowDigit = True
            else:
                resultStr = resultStr + txtNumber[int(ch)]


        # 1억 이상
        if digitCount > hundredMillionPos:
            if not notShowDigit:
                resultStr = resultStr + txtDigit[digitCount-hundredMillionPos]
        # 1만 이상
        elif digitCount > tenThousandPos:
            if not notShowDigit:
                resultStr = resultStr + txtDigit[digitCount-tenThousandPos]
        else:
            if not notShowDigit:
                resultStr = resultStr + txtDigit[digitCount]

        if digitCount <= 0:
            digitCount = 0
        else:
            digitCount = digitCount - 1
        index = index + 1
        if index >= len(strNum):
            break;
    #print(resultStr)
    return resultStr


if __name__ == '__main__':

    digit2txt("21,560,000.13")
    digit2txt("1234.13")
    digit2txt("1020340.13")
    digit2txt("22222330.13")
