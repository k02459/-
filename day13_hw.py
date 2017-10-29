import random as r    #랜덤 함수 불러오기
import turtle as t    #거북이 함수 불러오기
t.shape("turtle")     #모양 거북이로 바꾸기

#사각형 그리기
t.penup()           #거북이 꼬리들기
t.setx(-250)        #거북이의 x좌표를 -250으로 설정
t.sety(250)         #거북이의 y좌표를 250으로 설정
t.pendown()         #거북이 꼬리내리기    
t.pensize(2)

for i in range(4) :     #4번 반복
    t.forward(500)      #앞으로 500픽셀 전진
    t.right(90)         #오른쪽으로 90도 회전     

t.penup()               #원점으로 오기
t.setx(100)             #거북이 x좌표를 100으로 설정
t.sety(50)              #거북이 y좌표를 50으로 설정
t.pendown()    

for i in range(4) :    #장애물 그리기
    t.forward(100)     #한 변이 100픽셀인 사각형을 그린다
    t.right(90)

t.penup()
t.home()       


t.right(r.randrange(0,360))     #출발 각 랜덤지정

while True :                       #무한 반복
    
    t.forward(2)       #앞으로 2픽셀 전진(숫자 커질수록 속도 빨라짐)
    
    if t.xcor() >= 250 :                     #오른쪽 벽에 부딪혔을 때
        
        if 0 <= t.heading() <= 90 :          #거북이가 오른쪽 위 방향으로 향하고 있다면
            t.left(180 - 2 * t.heading())    #계산값 만큼 왼쪽으로 회전
        
        elif 270 <= t.heading() <= 360 :     #거북이가 오른쪽 아래 방향으로 향하고 있을 때
            t.right(2 * t.heading() - 540)    #계산값만큼 오른쪽으로 회전


    if t.xcor() <= -250 :   #왼쪽 벽에 부딪혔을 때도 같은 방식으로 코딩한다
        
        if 90 <= t.heading() <= 180 :      
            t.right(2 * t.heading() - 180)
        
        elif 180 <= t.heading() <= 270 :
            t.left(540 - 2 * t.heading())


    if t.ycor() >= 250 :        #위쪽 벽에 부딪혔을때도 같은 방식으로 코딩한다
        
        if 0 <= t.heading() <= 90 :
            t.right( 2 * t.heading() )

        elif 90 <= t.heading() <= 180 :
            t.left( 360 - 2 * t.heading() )


    if t.ycor() <= -250 :   #아래쪽 벽에 부딪혔을 때도 같은 방식으로 코딩한다
        
        if 270 <= t.heading() <= 360 :
            t.left( 720 - 2 * t.heading() )

        elif 180 <= t.heading() <= 270 :
            t.right( 2 * t.heading() - 360 )



    if 100 <= t.xcor() <= 200 and -50 <= t.ycor() <= 50 :     #장애물에 부딪혔을 때도 마찬가지로 코딩한다
        
        if abs(t.xcor() - 100) <= 2 :

            if 0 <= t.heading() <= 90 :             
                t.left(180 - 2 * t.heading())   
        
            elif 270 <= t.heading() <= 360 :
                t.right(2 * t.heading() - 540)

                
        if abs(t.xcor() - 200) <= 2 :

            if 90 <= t.heading() <= 180 :      
                t.right(2 * t.heading() - 180)
        
            elif 180 <= t.heading() <= 270 :
                t.left(540 - 2 * t.heading())


        if abs(t.ycor() - 50) <= 2 :

            if 270 <= t.heading() <= 360 :
                t.left( 720 - 2 * t.heading() )

            elif 180 <= t.heading() <= 270 :
                t.right( 2 * t.heading() - 360 )


        if abs(t.ycor() - (-50)) <= 2 :

            if 0 <= t.heading() <= 90 :
                t.right( 2 * t.heading() )

            elif 90 <= t.heading() <= 180 :
                t.left( 360 - 2 * t.heading())
