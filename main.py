from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.size = (350, 450)


class MainWidget(Widget):
    def clear(self):
        self.ids.input.text=""

    def back(self):
        expression = self.ids.input.text
        expression = expression[:1]
        self.ids.input.text = expression


    def pressed(self, button):
        expression = self.ids.input.text

        if "Fault" in expression:
            expression = ""

        if expression == "0":
            self.ids.input.text = ""
            self.ids.input.text = f"{button}"

        else:
            self.ids.input.text = f"{expression}{button}"

    def answer(self):
        expression = self.ids.input.text
        try:
            self.ids.input.text = str(eval(expression))

        except:
            self.ids.input.text = "Fault"

class TheLabApp(App):
    pass

TheLabApp().run()