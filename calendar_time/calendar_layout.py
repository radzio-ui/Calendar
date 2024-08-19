from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.layout import Layout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from kivy.uix.stacklayout import StackLayout
from kivy.logger import Logger
from calendar_time.calendar_time import CalDates
from events.events_layout import EventData


class CalendarData:
    curr_date = CalDates.current_month_and_year()
    event_list = tuple(['dumdumdum'] * 100)

    @classmethod
    def get_events_from_cur_month_onwards(cls):
        cls.event_list = tuple(['dumdumdum'] * 20)
        return cls.event_list


class FwdBtn(Button, ButtonBehavior):
    def __init__(self, **kwargs):
        super(FwdBtn, self).__init__(**kwargs)

    def on_btn_press(self):
        print("FORWARD BUTTON")
        # curframe = inspect.currentframe()
        # calframe = inspect.getouterframes(curframe, 2)
        # print('caller name:', calframe[1][3])
        new_date = CalDates.increase_one_month(CalendarData.curr_date)
        CalendarData.curr_date = new_date


class CalendarEventListLayout:
    def __init__(self, event_list: tuple = CalendarData.event_list, event_list_interval='monthly'):
        self.event_list = event_list
        self.event_layout = BoxLayout(orientation='vertical', size_hint=(1, 10))
        self.buttons_layout = GridLayout(cols=4, rows=1, size_hint=(1, 0.1))
        self.buttons_layout.add_widget(Label(text='Event list', size_hint=(0.85, None), height=20))
        for i in [1, 2, 4]:
            btn = Button(text=str(i), size_hint=(0.05, None), height=20)
            btn.on_press = lambda _i=i: self.redraw_event_list(cols=_i)
            self.buttons_layout.add_widget(btn)
        self.event_layout.add_widget(self.buttons_layout)

    def draw_event_list(self, cols: int = 1) -> Layout:
        Logger.info(f'Drawing EventListLayout (cols={str(cols)}) {str(self.event_list):60}')
        if hasattr(self, 'event_list_layout'):
            self.event_layout.remove_widget(self.event_list_layout)
            Logger.info('Clearing all widgets from EventListLayout')
        self.event_list_layout = GridLayout(cols=cols, spacing=1, size_hint=(1, 10))
        for i, event in enumerate(self.event_list):
            btn = Button(text='event ' + str(i), height=40)
            self.event_list_layout.add_widget(btn)
        self.event_layout.add_widget(self.event_list_layout)
        return self.event_layout

    def redraw_event_list(self, cols: int):
        self.draw_event_list(cols)


class CalendarDaysLayout:
    def __init__(self):
        self.calendar_layout = GridLayout(cols=7, spacing=1, size_hint=(1, 0.6))

        """Weekdays"""
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            self.calendar_layout.add_widget(Button(text=day, height=40))

    def draw_calendar(self, date):
        print('debug print, redrawing CalendarLayout')
        day = CalDates.month_day_start(date)
        # add empty fields to start adding days at correct position
        for _ in range(CalDates.rev_weekdays[day[0]] - 1):
            self.calendar_layout.add_widget(Label(text='', height=40))
        # add Buttons for each day in months starting at correct position
        for i in range(1, CalDates.days_in_month(CalendarData.curr_date) + 1):
            btn = Button(text=str(i), height=40)
            self.calendar_layout.add_widget(btn)
        return self.calendar_layout


class CalendarLayout(Screen):
    def __init__(self, **kwargs):
        super(CalendarLayout, self).__init__(**kwargs)
        """Layouts"""
        self.master = GridLayout(rows=3, cols=1, padding=(25, 25), size_hint=(1, 1))
        self.header = GridLayout(cols=3, rows=2, size_hint=(1, 0.15))

        """Draw calendar and event_list layouts"""
        self.calendar_layout = CalendarDaysLayout().draw_calendar(CalendarData.curr_date)
        self.calendar_layout.padding = (25, 25)
        self.event_layout = ScrollView()
        self.event_layout.padding = (25, 50)
        self.event_layout.add_widget(CalendarEventListLayout().draw_event_list())

        """Widgets"""
        self.btn1 = Button(text='main menu', size_hint_x=0.25, opacity=0.5)
        self.btn2 = Label(text='Your Calendar App', size_hint_x=1, opacity=1)
        self.btn3 = Button(text='X', size_hint_x=0.25, opacity=0.5)
        self.btn_backward = Button(text='<--', size_hint_x=0.25, opacity=0.75)
        self.current_month_label = Label(size_hint_x=1, opacity=1,
                                         text=CalDates.month_name(
                                             CalendarData.curr_date) + '   ' + CalendarData.curr_date[:4])
        self.btn_forward = FwdBtn(text='-->', size_hint_x=0.25, opacity=0.75)
        self.btn_forward.bind(on_press=self.on_press_fwd_btn)
        self.btn1.bind(on_press=self.go_to_main)

        """Packing layouts with widgets"""
        self.header.add_widget(self.btn1)
        self.header.add_widget(self.btn2)
        self.header.add_widget(self.btn3)
        self.header.add_widget(self.btn_backward)
        self.header.add_widget(self.current_month_label)
        self.header.add_widget(self.btn_forward)

        self.master.add_widget(self.header)
        self.master.add_widget(self.calendar_layout)
        self.master.add_widget(self.event_layout)

        self.add_widget(self.master)

    def on_press_fwd_btn(self, instance):
        self.calendar_layout.clear_widgets()
        self.btn_forward.on_btn_press()
        print('pressed fwd button')
        self.calendar_layout.add_widget(CalendarDaysLayout().draw_calendar(CalendarData.curr_date))
        self.current_month_label.text = CalDates.month_name(CalendarData.curr_date) + '   ' + CalendarData.curr_date[:4]

    def go_to_main(self, instance):
        pass
