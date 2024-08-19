from kivy.app import App
from kivy.logger import Logger
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

from calendar_time.calendar_layout import CalendarLayout
from events.events_layout import EventsWindow, CreateEventWindow
from login.login_layout import LoginWindow
from notes.notes_layout import NotesWindow
from settings.settings_layout import SettingsWindow


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        Logger.info('Entered Main Window')
        self.main_layout = BoxLayout()
        self.main_layout.orientation = "vertical"

        self.calendar_button = Button(text="Calendar", on_press=self.go_to_calendar)
        self.events_button = Button(text="Events", on_press=self.go_to_events)
        self.notes_button = Button(text="Notes", on_press=self.go_to_notes)
        self.settings_button = Button(text="Settings", on_press=self.go_to_settings)

        self.main_layout.add_widget(self.calendar_button)
        self.main_layout.add_widget(self.events_button)
        self.main_layout.add_widget(self.notes_button)
        self.main_layout.add_widget(self.settings_button)
        self.add_widget(self.main_layout)

    def go_to_calendar(self, instance):
        Logger.info('Going from Main Window to Calendar Window')

        app.root.current = "calendar"

    def go_to_events(self, instance):
        Logger.info('Going from Main Window to Events Window')

        app.root.current = "events"

    def go_to_notes(self, instance):
        Logger.info('Going from Main Window to Notes Window')

        app.root.current = "notes"

    def go_to_settings(self, instance):
        Logger.info('Going from Main Window to Settings Window')

        app.root.current = "settings"


class MyApp(App):
    def build(self):
        # self.root = BoxLayout(orientation="vertical")

        # Create and add views to screen manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(LoginWindow(name="login"))
        screen_manager.add_widget(MainWindow(name="main"))
        screen_manager.add_widget(CalendarLayout(name="calendar"))
        screen_manager.add_widget(EventsWindow(name="events"))
        screen_manager.add_widget(NotesWindow(name="notes"))
        screen_manager.add_widget(SettingsWindow(name="settings"))
        screen_manager.add_widget(CreateEventWindow(name="create_event"))
        CalendarLayout.go_to_main = self.go_to_main
        LoginWindow.go_to_main = self.go_to_main
        NotesWindow.go_to_main = self.go_to_main
        EventsWindow.go_to_main = self.go_to_main
        SettingsWindow.go_to_main = self.go_to_main
        EventsWindow.go_to_create_event = self.go_to_create_event
        # self.root.add_widget(self.screen_manager)
        return screen_manager

    def go_to_main(self, instance):
        app.root.current = 'main'

    def go_to_create_event(self, instance):
        app.root.current = 'create_event'


if __name__ == "__main__":
    app = MyApp()
    app.run()
