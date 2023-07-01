from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file(filename='Navek.kv')

class WindowManager(ScreenManager):
    pass

class Home(Screen):
    pass

class OtherScreen(Screen):
    pass

class MyApp(MDApp):

    def build(self):
        # Create a list of all screens, loop through it and add them to the screen manager
        screens = [
            Home(name="home_screen"),
            OtherScreen(name="other_screen")
        ]

        self.wm = WindowManager()

        for screen in screens:
            self.wm.add_widget(screen)

        return self.wm

if __name__ == "__main__":
    MyApp().run()
