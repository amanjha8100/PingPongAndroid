from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.lang.builder import Builder

Builder.load_string("""
<PongBall>:
    size: 50,50
    canvas:
        Ellipse:
            pos: self.pos
            size: self.size

<PongPaddle>:
    size: 25,200
    canvas:
        Rectangle:
            pos: self.pos
            size: self.size



<PongGame>:
    ball: pong_ball
    player1: player_left
    player2: player_right
    canvas:
        Rectangle:
            pos: self.center_x - 5, 0
            size: 10, self.height
    
    Label:
        font_size: 70
        center_x: root.width/4
        top: root.top - 50
        text: str(root.player2.score)

    Label:
        font_size: 70
        center_x: root.width * 3/4
        top: root.top - 50
        text: str(root.player1.score)

    PongBall:
        id: pong_ball
        center: self.parent.center

    PongPaddle:
        id:player_left
        x: root.x
        center_y: root.center_y

    PongPaddle:
        id:player_right
        x: root.width-self.width
        center_y: root.center_y
""")

class PongPaddle(Widget):
    score = NumericProperty(0)
    def bounce_ball(self,ball):
        #collide widget is a pre-defined function which check if two widgets have collided
        if self.collide_widget(ball):
            ball.velocity_x *= -1.01


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

#naming conventions and predefined
#on_touch_down() - when our fingers/mouse touches the screen
#on_touch_up() - when we lift our finger of the screen after touching it
#on_touch_move() - when we drag our finger on the screen

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self):
        self.ball.velocity = Vector(8,0).rotate(randint(0,360))

    def update(self, dt):
        #moving the ball by calling the move method 
        self.ball.move()
        if (self.ball.y < 0) or (self.ball.y > self.height-50):
            self.ball.velocity_y *= -1

        #bounce off left and increase score
        if self.ball.x < 0:
            self.ball.velocity_x *= -1
            self.player1.score += 1

        #bounce off right and increse score
        if self.ball.x > self.width-50:
            self.ball.velocity_x *= -1
            self.player2.score += 1

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)


    def on_touch_move(self, touch):
        if touch.x < self.width/ 1/2:
            self.player1.center_y = touch.y
        if touch.x > self.width * 1/2:
            self.player2.center_y = touch.y

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


PongApp().run()
