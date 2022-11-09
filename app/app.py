from kivy.app import App, Widget
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout


class CanvasExample1(Widget):
    pass


class CanvasExample2(Widget):
    pass


class WidgetsExample(GridLayout):
    count_enabled = BooleanProperty(False)
    count = 1
    my_text = StringProperty("H1")
    slider_val = StringProperty("50")
    text_input = StringProperty("fooo")

    def on_button_press(self):
        if self.count_enabled:
            print("btn clicked")
            self.count += 1
            self.my_text = str(self.count)

    def on_toggle_button_state(self, toggle_state):
        print('toggle state: ' + toggle_state.state)
        if toggle_state.state == 'normal':
            toggle_state.text = 'OFF'
            self.count_enabled = False

        else:
            toggle_state.text = 'ON'
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    def on_slider_value(self, widget):
        self.slider_val = str(int(widget.value))
        print("Slider: " + str(int(widget.value)))

    def on_text_validate(self, widget):
        self.text_input = widget.text


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "rl-bt"

        for i in range(1, 101):
            size = dp(100)
            b = Button(text=str(i), size_hint=(None, None), size=(size, size))
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
#     pass

class BoxLayoutExample(BoxLayout):
    pass
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"  # horizontal
        b1 = Button(text="1")
        b2 = Button(text="2")
        b3 = Button(text="3")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)"""


class MainWidget(Widget):
    pass


class MobileApp(App):
    pass


MobileApp().run()
