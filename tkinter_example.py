from tkinter import * #tkinter 라이브러리 전체 import


#-----------------tkinter setting section-----------------
root=Tk()
root.title("MOGRITHS")           # 제목
root.geometry("300x200+100+100") # ("너비 x 높이 + x좌표 + y좌표")
root.resizable(False,False)      # 윈도우 상하좌우 창 크기 조절
count=0

#-----------------function section-----------------
def countplus():        #button_section
    global count
    count+=1
    if count>10:
        count=10
        
    button_label.config(text=str(count))
    
def countminus():       #button_section
    global count
    count-=1
    if count<0:
        count=0
        
    button_label.config(text=str(count))

def calc(event):        #entry_section
    entry_label.config(text="계산결과: "+str(eval(entry.get())))

def currNum(self):      #scale_section
    value="현재 숫자: "+str(scale.get())
    scale_label.config(text=value)
    

#-----------------widget section-----------------
button_label=Label(root,text="0")
button1=Button(root,width=10,text="plus",overrelief="solid",command=countplus)
button2=Button(root,width=10,text="minus",overrelief="solid",command=countminus)

entry_label=Label(root,text="계산결과:")
entry=Entry(root,width=30)
entry.bind("<Return>",calc)

scale_label=Label(root,text="현재 숫자: 0")
scale=Scale(root,command=currNum,orient="horizontal",showvalue=False
            ,from_=0 ,to=255)

#-----------------pack section-----------------
button_label.pack()
button1.pack()
button2.pack()
entry_label.pack()
entry.pack()
scale_label.pack()
scale.pack()

root.mainloop()


'''
    1. 버튼의 속성
        command:버튼이 active 상태일 때 실행할 함수
        
    2. 엔트리의 속성
        get(): 기입창의 텍스트를 문자여로 반환
        eval(): 매개변수로 받은 expresstion(식)을 문자열로 받아 실행

    3. 슬라이더(scale)의 속성
        orient=vertical(horizontal): scale의표시 방향(세로 / 가로 순)
        from_: 슬라이더 최소값
        to:    슬라이더 최대값
        variable: Scale의 상태를 저장할 변수 (tkinter.Intvar())
        label: 슬라이더에 표시할 텍스트
        showvalue=True(False): 슬라이더의 현재 값 표시 여부

    4. 정수를 다루는 Tkinter의 Variable 인스턴스
        num=tkinter.IntVar() 
'''