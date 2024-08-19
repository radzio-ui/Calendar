from kivy import Logger
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


class LoginWindow(Screen):
    def __init__(self, **kwargs):
        super(LoginWindow, self).__init__(**kwargs)
        self.login_layout = BoxLayout()
        self.login_layout.orientation = "vertical"

        self.login_input = TextInput(hint_text="Login")
        self.password_input = TextInput(hint_text="Password", password=True)
        self.login_layout.add_widget(self.login_input)
        self.login_layout.add_widget(self.password_input)

        login_button = Button(text="Login", on_press=self.login)
        self.login_layout.add_widget(login_button)
        self.add_widget(self.login_layout)

    def login(self, instance):
        # Check login credentials and navigate to main window
        if self.login_input.text == "" and self.password_input.text == "":
            self.go_to_main(instance)
            Logger.info('Login successful. Going to Main Window')
        else:
            # Show error message
            Logger.info('Login unsuccessful. Try again.')

            pass

    def go_to_main(self, instance):
        pass
