from kivy.app import App
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from calendar_time.calendar_time import CalDates


class Data:
    curr_date = CalDates.current_month_and_year()


class FwdBtn(Button, ButtonBehavior):
    def __init__(self, **kwargs):
        super(FwdBtn, self).__init__(**kwargs)

    def on_press(self):
        nd = CalDates.increase_one_month(Data.curr_date)
        Data.curr_date = nd


class CalendarLayout:
    def __init__(self):
        self.calendar_layout = GridLayout(cols=7, spacing=1, size_hint_y=None)

        """Weekdays"""
        self.calendar_layout.add_widget(Button(text='Monday', size_hint_y=None, height=40))
        self.calendar_layout.add_widget(Button(text='Tuesday', size_hint_y=None, height=40))
        self.calendar_layout.add_widget(Button(text='Wednesday', size_hint_y=None, height=40))
        self.calendar_layout.add_widget(Button(text='Thursday', size_hint_y=None, height=40))
        self.calendar_layout.add_widget(Button(text='Friday', size_hint_y=None, height=40))
        self.calendar_layout.add_widget(Button(text='Saturday', size_hint_y=None, height=40))
        self.calendar_layout.add_widget(Button(text='Sunday', size_hint_y=None, height=40))

    def draw_calendar(self, date):
        print('debug print, redrawing CalendarLayout')
        day = CalDates.month_day_start(date)
        for _ in range(CalDates.rev_weekdays[day[0]] - 1):
            self.calendar_layout.add_widget(Label(text='', size_hint_y=None, height=40))
        for i in range(1, CalDates.days_in_month(Data.curr_date) + 1):
            btn = Button(text=str(i), size_hint_y=None, height=40)
            self.calendar_layout.add_widget(btn)
        return self.calendar_layout


class CalApp(App):
    def build(self):
        """Layouts"""
        self.master = GridLayout(rows=3)
        self.header = GridLayout(cols=3, rows=2, size_hint=(1, None), size=(Window.width, Window.height * 0.1))
        self.scroll_layout = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.9))

        """Widgets"""
        self.btn1 = Button(text='menu', size_hint_x=0.25)
        self.btn2 = Label(text='Your Calendar App', size_hint_x=0.7)
        self.btn3 = Button(text='X', size_hint_x=0.05)
        self.btn_backward = Button(text='<--')
        self.current_month_label = Label(text=CalDates.month_name(Data.curr_date))
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
        self.master.add_widget(self.scroll_layout)
        self.scroll_layout.add_widget(CalendarLayout().draw_calendar(Data.curr_date))
        return self.master

    def on_press_fwd_btn(self, instance):
        self.root.clear_widgets()
        print('pressed fwd button')
        FwdBtn().on_press()

        self.root = GridLayout(rows=3)
        self.header = GridLayout(cols=3, rows=2, size_hint=(1, None), size=(Window.width, Window.height * 0.1))
        self.scroll_layout = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.9))
        """Widgets"""
        self.btn1 = Button(text='menu', size_hint_x=0.25)
        self.btn2 = Label(text='Your Calendar App', size_hint_x=0.7)
        self.btn3 = Button(text='X', size_hint_x=0.05)
        self.btn_backward = Button(text='<--')
        self.current_month_label = Label(text=CalDates.month_name(Data.curr_date))
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
        self.master.add_widget(self.scroll_layout)
        self.scroll_layout.add_widget(CalendarLayout().draw_calendar(Data.curr_date))
        return self.master


CalApp().run()
