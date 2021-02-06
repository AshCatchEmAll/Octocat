from turtle import Turtle
from turtle import Screen

octolegs = [
(-26.0, 39.0),
(-31.0, 36.0),
(-35.0, 33.0),
(-37.0, 25.0),
(-38.0, 16.0),
(-38.0, 5.0),
(-38.0, -9.0),
(-37.0, -25.0),
(-37.0, -45.0),
(-43.0, -61.0),
(-49.0, -74.0),
(-63.0, -87.0),
(-73.0, -96.0),
(-68.0, -97.0),
(-58.0, -97.0),
(-44.0, -87.0),
(-33.0, -70.0),
(-26.0, -55.0),
(-23.0, -36.0),
(-17.0, -19.0),
(-14.0, -13.0),
(-9.0, -5.0),
(-6.0, -6.0),
(-6.0, -12.0),
(-4.0, -23.0),
(-3.0, -40.0),
(-3.0, -58.0),
(-3.0, -72.0),
(-3.0, -83.0),
(-9.0, -91.0),
(-12.0, -94.0),
(-6.0, -100.0),
(4.0, -99.0),
(12.0, -92.0),
(15.0, -77.0),
(14.0, -58.0),
(13.0, -34.0),
(17.0, -16.0),
(19.0, -5.0),
(29.0, -2.0),
(35.0, -2.0),
(38.0, -5.0),
(39.0, -12.0),
(42.0, -28.0),
(44.0, -39.0),
(47.0, -54.0),
(50.0, -69.0),
(54.0, -84.0),
(57.0, -92.0),
(62.0, -94.0),
(75.0, -94.0),
(82.0, -91.0),
(81.0, -83.0),
(76.0, -80.0),
(68.0, -75.0),
(65.0, -61.0),
(61.0, -49.0),
(60.0, -32.0),
(57.0, -13.0),
(57.0, 1.0),
(60.0, 4.0),
(71.0, 5.0),
(79.0, -0.0),
(84.0, -9.0),
(90.0, -24.0),
(94.0, -42.0),
(97.0, -59.0),
(105.0, -75.0),
(117.0, -80.0),
(130.0, -79.0),
(136.0, -75.0),
(136.0, -67.0),
(129.0, -67.0),
(118.0, -63.0),
(109.0, -54.0),
(104.0, -33.0),
(100.0, -16.0),
(91.0, 6.0),
(80.0, 20.0),
(68.0, 37.0),
(60.0, 43.0),
(49.0, 47.0),
(37.0, 49.0),
(20.0, 49.0),
(6.0, 48.0),
(-8.0, 47.0),
(-20.0, 42.0),
(-28.0, 37.0)
]

insideCircle = [(-47.0 ,122.0),
(-23.0 ,123.0),
(-8.0 ,121.0),
(1.0 ,118.0),
(7.0, 116.0),
(14.0 ,117.0),
(19.0 ,121.0),
(26.0 ,125.0),
(37.0 ,130.0),
(50.0, 130.0),
(63.0 ,121.0),
(65.0 ,107.0),
(65.0 ,91.0),
(64.0, 80.0),
(53.0 ,67.0),
(26.0 ,60.0),
(-7.0, 55.0),
(-30.0 ,57.0),
(-44.0, 68.0),
(-53.0 ,83.0),
(-58.0, 97.0),
(-58.0 ,115.0),(-47.0 ,122.0)]

outerLeg = [
	(-37.0, -23.0),
(-48.0, -26.0),
(-54.0, -33.0),
(-68.0, -36.0),
(-82.0, -35.0),
(-99.0, -29.0),
(-106.0, -19.0),
(-117.0, -16.0),
(-127.0, -22.0),
(-133.0, -25.0),
(-131.0, -30.0),
(-126.0, -32.0),
(-117.0, -32.0),
(-110.0, -32.0),
(-102.0, -36.0),
(-93.0, -45.0),
(-77.0, -50.0),
(-55.0, -51.0),
(-43.0, -41.0),
(-36.0, -35.0),
(-35.0, -29.0),
(-37.0, -24.0),
(-38.0, -22.0),
(-38.0, -50.0),


]
shadeLeg = [
	(-37.0, -46.0),
(-45.0, -50.0),
(-55.0, -54.0),
(-71.0, -55.0),
(-85.0, -53.0),
(-97.0, -44.0),
(-103.0, -35.0),
(-95.0, -43.0),
(-84.0, -48.0),
(-73.0, -50.0),
(-56.0, -50.0),
(-49.0, -44.0),
(-40.0, -38.0),
(-35.0, -36.0),
(-36.0, -48.0),
]

circles = [
	(-53.0, -41.0),
(-69.0, -43.0),
(-87.0, -42.0),
(-110.0, -27.0)
]

leftEye = [(-23.0, 101.0),
(-28.0, 101.0),
(-31.0, 96.0),
(-31.0, 91.0),
(-30.0, 85.0),
(-28.0, 81.0),
(-24.0, 78.0),
(-20.0, 78.0),
(-16.0, 79.0),
(-15.0, 87.0),
(-15.0, 94.0),
(-19.0, 99.0),
(-21.0, 101.0),
(-26.0, 101.0),]

rightEye = [(38.0, 110.0),
(34.0, 106.0),
(33.0, 100.0),
(37.0, 93.0),
(42.0, 89.0),
(46.0, 89.0),
(50.0, 94.0),
(50.0, 103.0),
(47.0, 112.0),
(40.0, 112.0),
(34.0, 107.0),
(34.0, 102.0),]

scarySmile = [
(2.0, 67.0),
(7.0, 63.0),
(17.0, 62.0),
(23.0, 64.0),
(26.0, 68.0),
(28.0, 70.0)
]

leftEar = [
	(-62.0, 139.0),
(-65.0, 151.0),
(-65.0, 163.0),
(-62.0, 172.0),
(-61.0, 175.0),
(-54.0, 172.0),
(-46.0, 167.0),
(-41.0, 162.0),
(-37.0, 158.0),
(-35.0, 156.0),
(-61.0, 141.0)
]


rightEar = [
(30.0, 160.0),
(32.0, 168.0),
(35.0, 176.0),
(44.0, 180.0),
(49.0, 181.0),
(54.0, 179.0),
(57.0, 170.0),
(57.0, 160.0),
(55.0, 153.0),
(53.0, 149.0)
]


height = 1000
width = 500
screen = Screen()
screen.screensize(width, height)


textOne = Turtle()
textOne.penup()
textOne.goto(-202.0, 216.0)
textOne.pendown()
textOne.write("'Scary octocat doesn't exist'")
textOne.hideturtle()

textTwo = Turtle()
textTwo.penup()
textTwo.goto(-201.0, 182.0)
textTwo.pendown()
textTwo.write("Scary octocat : ")
textTwo.hideturtle()

github = Turtle()
github.penup()
github.goto(0,100)
github.pendown()
github.shape("circle")
github.shapesize(6,8,10)
github.fillcolor("black")
inner = Turtle()
inner.penup()
inner.goto(insideCircle[0])
inner.pendown()
inner.color("#F7C9B6")
inner.begin_fill()
for i in insideCircle:
	inner.goto(i)
inner.end_fill()
inner.hideturtle()


legs = Turtle()
legs.penup()
legs.goto(octolegs[0])
legs.pendown()
legs.color("black")
legs.begin_fill()
for i in octolegs:
	
	legs.goto(i)
legs.end_fill()
legs.hideturtle()
 
outerleg = Turtle()
outerleg.penup()
outerleg.goto(-37.0, -22.0)
outerleg.pendown()
outerleg.color("#101010")
outerleg.begin_fill()
for i in outerLeg:

	outerleg.goto(i)
outerleg.end_fill()
outerleg.hideturtle()

shadeleg = Turtle()
shadeleg.penup()
shadeleg.goto(-37.0, -46.0)
shadeleg.pendown()
shadeleg.color("black")
shadeleg.begin_fill()
for i in shadeLeg:

	shadeleg.goto(i)
shadeleg.end_fill()
shadeleg.hideturtle()


circle = Turtle()
circle.penup()
circle.goto(-53.0, -41.0)
circle.pendown()
for i in circles:
	circle.penup()
	circle.goto(i)
	circle.color("#D2E5D0")
	circle.begin_fill()
	circle.pendown()
	circle.circle(5)
	circle.end_fill()
circle.hideturtle()

lefteye = Turtle()
lefteye.penup()
lefteye.goto(leftEye[0])
lefteye.pendown()
lefteye.color("white")
lefteye.begin_fill()
for i in leftEye:
	lefteye.goto(i)
lefteye.end_fill()
lefteye.hideturtle()

righteye = Turtle()
righteye.penup()
righteye.goto(rightEye[0])
righteye.pendown()
righteye.color("white")
righteye.begin_fill()
for i in rightEye:
	righteye.goto(i)
righteye.end_fill()
righteye.hideturtle()


innerLeftEye = Turtle()
innerLeftEye.penup()
innerLeftEye.goto(-23.0, 89.0)
innerLeftEye.pendown()
innerLeftEye.shape("circle")
innerLeftEye.shapesize(0.4,0.3,0.5)
innerLeftEye.fillcolor("#F7C9B6")

innerRightEye = Turtle()
innerRightEye.penup()
innerRightEye.goto(42.0, 100.0)
innerRightEye.pendown()
innerRightEye.shape("circle")
innerRightEye.shapesize(0.4,0.3,0.5)
innerRightEye.fillcolor("#F7C9B6")

nose = Turtle()
nose.penup()
nose.goto(12.0, 83.0)
nose.pendown()
nose.shape("circle")
nose.shapesize(0.3,0.4,0.5)
nose.fillcolor("#DBC39A")

scarysmile = Turtle()
scarysmile.penup()
scarysmile.goto(scarySmile[0])
scarysmile.pendown()
scarysmile.color("#FB6090")
scarysmile.pensize(5)
for i in scarySmile:
	scarysmile.goto(i)
scarysmile.end_fill()
scarysmile.hideturtle()


leftear = Turtle()
leftear.penup()
leftear.goto(leftEar[0])
leftear.pendown()
leftear.color("black")
leftear.begin_fill()
for i in leftEar:
	leftear.goto(i)
leftear.end_fill()
leftear.hideturtle()

rightear = Turtle()
rightear.penup()
rightear.goto(rightEar[0])
rightear.pendown()
rightear.color("black")
rightear.begin_fill()
for i in rightEar:
	rightear.goto(i)
rightear.end_fill()
rightear.hideturtle()


textThree = Turtle()
textThree.penup()
textThree.goto(78.0, -184.0)
textThree.pendown()
textThree.write("By team A.S.K")
textThree.hideturtle()

