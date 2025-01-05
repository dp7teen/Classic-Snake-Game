import turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for n in range(3):
            new_segment = turtle.Turtle("square")
            self.segments.append(new_segment)

        for body in range(len(self.segments)):
            if body == 0:
                self.segments[body].color("white")
                self.segments[body].goto(0, 0)
                print(self.segments[body].pos())
                posi = self.segments[body].pos()
            else:
                next_pos = posi[0] - 20
                posi = [next_pos, 0]
                posi = tuple(posi)
                self.segments[body].color("white")
                self.segments[body].penup()
                self.segments[body].goto(next_pos, 0)
                print(self.segments[body].pos())

    def move(self):
        for n in range(len(self.segments) - 1, 0, -1):
            self.segments[n].penup()
            x = self.segments[n - 1].xcor()
            y = self.segments[n - 1].ycor()
            self.segments[n].goto(x, y)
        self.head.penup()
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        tail_x = self.segments[len(self.segments) - 1].xcor()
        tail_y = self.segments[len(self.segments) - 1].ycor()
        new_segment.goto(tail_x - 20, tail_y - 20)
        self.segments.append(new_segment)
