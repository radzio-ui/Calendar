from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class SettingsWindow(Screen):
    def __init__(self, **kwargs):
        super(SettingsWindow, self).__init__(**kwargs)
        self.orientation = "vertical"

        # TODO: Implement settings view

        back_button = Button(text="Back to Main", on_press=self.go_to_main)
        self.add_widget(back_button)

    def go_to_main(self, instance):
        pass