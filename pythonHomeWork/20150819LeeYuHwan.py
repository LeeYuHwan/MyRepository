from redBlackTree import *
from AVLTree import *
from doubleHashing import *

import random, time
print("20150819이유환 중간고사 과제")

f = open( "data.txt", "r", encoding="utf-8" )
lines = f.readlines()
tmp = ""
addData = ""
for line in lines:
    tmp += line
f.close()

data = tmp.split("\n")
title = []
addTxt = ""

for i in range(0, len(data)):
    title.append(data[i][0:data[i].find(":")])

while True:
    print("S[검색], A[추가], Q[종료]");
    start = input()
    if start == "S":   
        print("다음중 검색할 정보의 제목을 입력하세요.")
        print(title)       
        search_title = input()

        print("검색에 사용할 알고리즘을 선택하세요.")
        print("1:레드-블랙 트리, 2:AVL, 3:이중해싱")
        choice = int(input())
        sw = 1
        if choice == 1 :
            key=data        

            d=Dict()
            for i in range(0, len(title)):
                d.insert(key[i])

            start_time=time.time()
            result=d.search(search_title)
            if result!=None :
                if result[0:result.find(":")] == search_title:
                    print('탐색완료 "' + search_title + '" 단어를 찾았습니다.')
                    print(result);                
            else :
                print('탐색오류 "' + search_title + '" 단어가 없습니다.')
                sw = 0                   
            elapsed_time=time.time()-start_time
            print('레드 블랙 트리 탐색의 실행시간 (N=%d) : %0.3f'
                %(len(title), elapsed_time))

        elif choice == 2 :
            key=data
    
            d=AVLDict()
            for i in range(0, len(title)):
                d.insert(key[i])

            start_time=time.time()
            result=d.search(search_title)
            if result!=None :
                if result[0:result.find(":")] == search_title:
                    print('탐색완료 "' + search_title + '" 단어를 찾았습니다.')
                    print(result);                
            else :
                print('탐색오류 "' + search_title + '" 단어가 없습니다.')
                sw = 0 
            elapsed_time=time.time()-start_time
            print('AVL 트리 탐색의 실행시간 (N=%d) : %0.3f'%(len(title), elapsed_time))
            print('완료')
            
        elif choice == 3 :
            M=len(title) + 3

            key=data
            d=HashingDict(M)
            for i in range(0, len(title)):
                d.insert(len(title) - 1,key[i], M)
           
            start_time=time.time()
            result=d.search(len(title) - 1, search_title, M)
            if result!=None :
                if result[0:result.find(":")] == search_title:
                    print('탐색완료 "' + search_title + '" 단어를 찾았습니다.')
                    print(result);                
            else :
                print('탐색오류 "' + search_title + '" 단어가 없습니다.')
                sw = 0 
            elapsed_time=time.time()-start_time
            print('이중 해싱의 실행시간 (N=%d) : %0.3f'%(len(title), elapsed_time))
            print('완료')

        else :
            print("1~3을 입력하세요.")

        if sw == 0 :
            print(search_title + "이 단어장에 없으므로 내용 추가를 실시합니다.")
            print(search_title + "의 내용을 입력하세요.")           
            addTmp = input()
            addData += search_title + ":" + addTmp
            data.append(addData)
            title.append(addData[0:addData.find(":")])
            addTxt += "\n"+addData
            addTmp = ""
            addData = ""            
            sw = 1

    elif start == "A":
        print("[추가] 를 선택하셨습니다.")
        print("[제목]:[내용] 양식에 맞춰서 작성하여 주십시오.")
        addTmp = input()
        addData += addTmp
        data.append(addData)
        title.append(addData[0:addData.find(":")])
        addTxt += "\n"+addData
        addTmp = ""
        addData = ""
        
    elif start == "Q":
        if addTxt != "" :
            f2 = open("data.txt","a", encoding="utf-8")
            f2.write(addTxt);
            f2.close()
        print("프로그램을 종료합니다.")
        break;
    else :
        print("S, A, Q 중에 하나를 입력하여주세요.")