from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivymd.uix.pickers import MDDatePicker

class EventData:
    fields = ["name", "type", "event_date_start", "event_date_end", "event_type", "notes", "cyclic", "notification"]
    event_list = tuple(['dumdumdum'] * 10)

    @classmethod
    def get_events_from_cur_month_onwards(cls):
        cls.event_list = tuple(['dumdumdum'] * 10)
        return cls.event_list


class EventsWindow(Screen):
    def __init__(self, **kwargs):
        super(EventsWindow, self).__init__(**kwargs)
        self.event_window_layout = BoxLayout()
        self.orientation = "vertical"

        CreateEventWindow()
        back_button = Button(text="Back to Main", on_press=self.go_to_main)
        create_button = Button(text="Create Event", on_press=self.go_to_create_event)
        self.event_window_layout.add_widget(back_button)
        self.event_window_layout.add_widget(create_button)
        self.add_widget(self.event_window_layout)

    def go_to_main(self, instance):
        pass

    def go_to_create_event(self, instance):
        pass


class CreateEventWindow(Screen):
    def __init__(self, **kwargs):
        super(CreateEventWindow, self).__init__(**kwargs)
        self.create_event_layout = GridLayout(cols=2, rows=len(EventData.fields) + 2, padding=(50, 20))
        self.draw_create_event_layout()
        self.add_widget(self.create_event_layout)

    def draw_create_event_layout(self):
        self.create_event_layout.add_widget(Label(text="Create New Event!", size_hint=(0.95, 1)))
        self.create_event_layout.add_widget(Button(text="X", size_hint=(0.05, 1)))

        for _, field in zip(range(len(EventData.fields)), EventData.fields):
            self.create_event_layout.add_widget(
                Label(text=field, height=40, halign='center', valign='middle', bold=True))
            if field in ["event_date_start", "event_date_end"]:
                date = MDDatePicker()
                self.create_event_layout.add_widget(date)
            else:
                self.create_event_layout.add_widget(TextInput(hint_text=field))
        self.create_event_layout.add_widget(Button(text="Cancel"))
        self.create_event_layout.add_widget(Button(text="Save"))
        return self.create_event_layout


class ShowEventWindow(Screen):
    def __init__(self, **kwargs):
        super(ShowEventWindow, self).__init__(**kwargs)


class EditEventWindow(Screen):
    def __init__(self, **kwargs):
        super(EditEventWindow, self).__init__(**kwargs)
