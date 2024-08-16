import inspect
from collections.abc import Sized, Iterable
from time import time

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout

from calendar_time.calendar_time import CalDates


class Data:
    curr_date = CalDates.current_month_and_year()
    event_list = tuple(['dumdumdum'] * 10)

    @classmethod
    def get_events_from_cur_month_onwards(cls):
        cls.event_list = tuple(['dumdumdum'] * 10)
        return cls.event_list


class FwdBtn(Button, ButtonBehavior):
    def __init__(self, **kwargs):
        super(FwdBtn, self).__init__(**kwargs)

    def on_btn_press(self):
        print("FORWARD BUTTON")
        # curframe = inspect.currentframe()
        # calframe = inspect.getouterframes(curframe, 2)
        # print('caller name:', calframe[1][3])
        new_date = CalDates.increase_one_month(Data.curr_date)
        Data.curr_date = new_date


class CalendarLayout:
    def __init__(self):
        self.calendar_layout = GridLayout(cols=7, spacing=1, size_hint_y=None)

        """Weekdays"""
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            self.calendar_layout.add_widget(Button(text=day, size_hint_y=None, height=40))

    def draw_calendar(self, date):
        print('debug print, redrawing CalendarLayout')
        day = CalDates.month_day_start(date)
        for _ in range(CalDates.rev_weekdays[day[0]] - 1):
            self.calendar_layout.add_widget(Label(text='', size_hint_y=None, height=40))
        for i in range(1, CalDates.days_in_month(Data.curr_date) + 1):
            btn = Button(text=str(i), size_hint_y=None, height=40)
            self.calendar_layout.add_widget(btn)
        return self.calendar_layout


class EventListLayout:
    def __init__(self, event_list: tuple = Data.event_list):
        self.event_list = event_list
        self.event_list_layout = BoxLayout(orientation='vertical', spacing=1)

    def draw_event_list(self):
        print('debug print, redrawing EventListLayout')
        for _ in range(len(self.event_list)):
            self.event_list_layout.add_widget(Label(text='', size_hint_y=None, height=40))
        for event in self.event_list:
            btn = Button(text=event, size_hint_y=None, height=40)
            self.event_list_layout.add_widget(btn)
        return self.event_list_layout


class CalApp(App):
    def build(self, new_month=Data.curr_date):
        """Layouts"""
        self.master = StackLayout(orientation='tb-lr')
        self.header = GridLayout(cols=3, rows=2, size_hint=(1, None), size=(Window.width, Window.height * 0.1))
        self.calendar_layout = GridLayout(cols=7, rows=5, size_hint=(1, None))
        self.event_layout = ScrollView()

        """Widgets"""
        self.btn1 = Button(text='menu', size_hint_x=0.25)
        self.btn2 = Label(text='Your Calendar App', size_hint_x=0.7)
        self.btn3 = Button(text='X', size_hint_x=0.05)
        self.btn_backward = Button(text='<--')
        self.current_month_label = Label(
            text=CalDates.month_name(new_month) + '   ' + new_month[:4])
        self.btn_forward = FwdBtn(text='-->')
        self.btn_forward.bind(on_press=self.on_press_fwd_btn)

        """Packing layouts with widgets"""
        self.header.add_widget(self.btn1)
        self.header.add_widget(self.btn2)
        self.header.add_widget(self.btn3)
        self.header.add_widget(self.btn_backward)
        self.header.add_widget(self.current_month_label)
        self.header.add_widget(self.btn_forward)
        self.master.add_widget(self.header)
        self.master.add_widget(self.calendar_layout)

        self.calendar_layout.add_widget(CalendarLayout().draw_calendar(new_month))
        self.event_layout.add_widget(EventListLayout().draw_event_list())
        self.master.add_widget(self.event_layout)
        return self.master

    def on_press_fwd_btn(self, instance):
        self.calendar_layout.clear_widgets()
        self.btn_forward.on_btn_press()
        print('pressed fwd button')
        self.calendar_layout.add_widget(CalendarLayout().draw_calendar(Data.curr_date))
        self.current_month_label.text = CalDates.month_name(Data.curr_date) + '   ' + Data.curr_date[:4]


CalApp().run()
