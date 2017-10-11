##201602459 김예림

import turtle as t      #거북이 라이브러리 불러오기
t.hideturtle()          #거북이 모양을 숨긴다
t.pencolor("black")     #펜 색 지정
t.bgcolor("black")      #배경 색 지정
t.speed(0)              #펜 속도 가장 빠르게

#그림 시작할 곳으로 이동
t.rt(90)
t.fd(400)

#벤치
t.pencolor("peru")      #펜 색 지정
t.fillcolor("peru")     #도형을 채울 색 지정
t.begin_fill()          #도형 채우기 시작
t.rt(90)
t.fd(250)

#의자왼쪽
for x in range(2) :     #반복함수    
    t.rt(90)
    t.fd(50)    
    t.rt(90)    
    t.fd(30)    
    t.lt(90)    
    t.fd(15)    
    t.lt(90)    
    t.fd(30)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(500)

#의자오른쪽
for x in range(2) :
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(30)
    t.lt(90)
    t.fd(15)
    t.lt(90)
    t.fd(30)
t.rt(90)
t.fd(50)
t.end_fill()        #도형 채우기 끝

#의자구멍뚫기
t.fillcolor("black")
t.rt(90)
t.fd(60)
t.begin_fill()
t.rt(90)
t.fd(65)
t.lt(90)
t.fd(380)
t.lt(90)
t.fd(15)
t.lt(90)
t.fd(380)
t.lt(90)
t.fd(80)
t.lt(90)
t.fd(380)
t.lt(90)
t.fd(15)
t.lt(90)
t.fd(380)
t.end_fill()

##
t.fillcolor("cadetblue")
t.lt(90)
t.fd(65)
t.begin_fill()
t.pencolor("black")
t.lt(30)
t.fd(60)
t.lt(30)
t.fd(40)
t.lt(30)
t.fd(80)
t.lt(30)
t.fd(40)
t.lt(30)
t.fd(60)
t.end_fill()

#여자
t.fillcolor("lightpink")
t.begin_fill()
t.rt(180)
t.fd(60)
t.lt(90)
t.fd(40)
t.lt(30)
t.fd(40)
t.lt(50)
t.fd(95)
t.end_fill()
t.pencolor("lightpink")

#머리
t.lt(150)
t.fd(150)
t.fillcolor("gray")
t.begin_fill()
t.circle(40)            #반지름이 ()인 원 그리기
t.end_fill()
t.pencolor("cadetblue")
t.rt(5)
t.fd(80)
t.fillcolor("darkgray")
t.begin_fill()
t.circle(45)
t.end_fill()
t.pencolor("darkgray")
t.lt(125)
t.fd(75)
t.rt(50)

##폭죽

#폭죽 올라가는 길
t.speed(1)          #가장 느린 속도
for x in range(13):
    t.pencolor("yellow")
    t.fd(5)    
    t.pencolor("black")    
    t.fd(15)

#폭죽 세번
t.speed(0)      #가장 빠른 속도
for x in range(40):
    t. fd(150)
    t.pencolor("fuchsia")
    t.pensize(10)    
    t.fd(50)    
    t.lt(180)    
    t.fd(50)    
    t.pensize(1)    
    t.pencolor("yellow")    
    t.fd(150)    
    t.lt(190)
t.pencolor("black")
t.lt(70)
t.fd(350)
for x in range(40):
    t. fd(80)
    t.pensize(10)
    t.pencolor("cyan")
    t.fd(35)
    t.lt(180)
    t.fd(35)
    t.pensize(3)
    t.pencolor("white")
    t.fd(80)
    t.lt(190)
t.pencolor("black")
t.lt(100)
t.fd(330)
t.lt(45)
t.fd(350)
for x in range(40):
    t. fd(100)
    t.pensize(15)
    t.pencolor("springgreen")
    t.fd(40)
    t.lt(180)
    t.fd(40)
    t.pensize(2)
    t.pencolor("white")
    t.fd(100)
    t.lt(170)
