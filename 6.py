from turtle import *

tracer(0)
lt(90)
down()
r = 10

##########################################################

for i in range(2):
    fd(21 * r)
    rt(90)
    fd(27 * r)
    rt(90)

up()
fd(9 * r)
rt(90)
fd(10 * r)
lt(90)
down()

for i in range(2):
    fd(86 * r)
    rt(90)
    fd(47 * r)
    rt(90)

#########################################################

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, "blue")

update()
while True: input()
