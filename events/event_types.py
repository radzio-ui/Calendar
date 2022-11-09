"""
File to store event properties for sorting purposes
"""
from datetime import datetime


class Event:
    def __init__(self, name, event_date_start, event_date_end=None, event_type='Event', notes=''):
        self._event_type = event_type
        self._event_date_start: datetime = event_date_start
        self.event_date_end = event_date_end
        if event_date_end is not None:
            self._event_date = f'from {event_date_start} to {event_date_end}'
        self._notes: str = notes
        self._note_count = 1
        self._name = name

    """the type"""

    @property
    def event_type(self):
        return self._event_type

    """the name"""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        self._name = v

    """creation date"""

    @property
    def creation_date(self):
        return self.__creation_date

    """setting the notes"""

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, value: str):
        if self._notes in value:
            s, e = value.find(self._notes), len(self._notes)
            value = value[0:s] + value[e:]
        self._notes += f'{self._note_count}: {value}\n'

        self._note_count += 1

    """setting the date"""

    @property
    def event_date(self):
        return self._event_date

    @event_date.setter
    def event_date(self, other: datetime):
        self._event_date = other

    def __str__(self):
        if self.event_date_end is None:
            return f'Event {self.event_type}, at {self._event_date}, notes:\n{self._notes}'
        return f'Event {self.event_type}, {self._event_date}, notes:\n{self._notes}'

    @staticmethod
    def save_event(user, event):
        with open(user + '.txt', 'at', encoding='utf-8') as f:
            f.write(str(event.__dict__))

    @staticmethod
    def load_event(user):
        with open(user + '.txt', 'at', encoding='utf-8') as f:
            return f.read()


class Birthday(Event):
    def __init__(self, name, event_date_start, event_date_end=None, event_type='Birthday', notes=''):
        super().__init__(name, event_date_start, event_date_end, notes)
        self._event_type = event_type
        self._event_date: datetime = event_date_start
        self.event_date_end = event_date_end
        if event_date_end is not None:
            self._event_date = f'from {event_date_start} to {event_date_end}'
        self._notes: str = notes
        self._note_count = 1
        self._name = name
        now = datetime.now()
        self.__creation_date = now.strftime("%Y_%m_%d")


class Home(Event):
    ...


class MeMySelfAndI(Event):
    ...


class Car(Event):
    ...
