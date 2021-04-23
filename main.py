from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
import random
from kivy.uix.popup import Popup


#First Popup
class MyPopUp(Popup):
    def __init__(**kwargs):
        super().__init__(**kwargs)
        self.l1 = Button(
            text="Press",
            background_color = "red",
        )
        self.l1.bind(on_press = self.bttn_action)
        self.size_hint=(0.5,0.5)
        self.title = "Toss"

        self.add_widget(self.l1)

    def bttn_action(self,instance):
        self.dismiss()

#result popup
class MyPop(Popup):
    def __init__(self,**kwargs):
        self.l2 = Button(
            text="Press",
            background_color = "blue",
        )
        self.size_hint = (0.5,0.5)
        self.title = "Result"

        self.add_widget(self.l2)

    def bttn_action2(self,instance):
        pass

class FirstWindow(Screen):
    def show(self):
        player1_name = ObjectProperty(None)
        player2_name = ObjectProperty(None)

    def shownow(self): #to generate a random number
        self.toss = [self.player1_name,self.player2_name]
        #print(self.toss[0],self.toss[1])
        self.rand_number = random.choice([0,1])
        return self.toss[self.rand_number]

    def open_pop_up(self):
        pops = MyPopUp()

        pops.l1.text = str(self.shownow()) + " won the toss! "+"\n Click to start game"

        tee = str(self.shownow())
        pops.open()


class Tab2(GridLayout):
    def __init__(self,**kwargs):
        self.option = ["0","X"]

        self.count = 0
        self.padding = (20,20)

        #user input
        self.current_value = 2
        super().__init__(**kwargs)
        self.cols = 3
        self.rows = 4
        self.lables = Button(text="choose \neither \nX / O", font_size=18,dis)