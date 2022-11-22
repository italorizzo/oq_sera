import turtle
amor = turtle.Turtle()
amor.screen.bgcolor('black')
amor.pensize(2)
amor.color('green')
amor.left(90)
amor.backward(100)
amor.speed(0)
def tree(i):
    if i < 10:
        return
    else:
        amor.forward(i)
        amor.color('red')
        amor.circle(2)
        amor.color('brown')
        amor.left(30)
        tree(3*i/4)
        amor.right(60)
        tree(3*i/4)
        amor.left(30)
        amor.backward(i)

tree(100)
turtle.done()