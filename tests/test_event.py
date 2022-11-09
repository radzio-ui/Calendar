from events.event_types import Event, Birthday
from datetime import datetime

test_date_start = datetime(2022, 12, 31)
test_date_end = datetime(2024, 1, 1)
test_notes = 'i want to do somethign'


def test_event():
    e = Event(name='zona moja', event_date_start=test_date_start, notes=test_notes)
    print(e)
    print(type(e))
    assert e.notes
    assert e._event_date
    assert isinstance(e, Event)


def test_birthday():
    birthday1 = Birthday('los_super_ktos', event_date_start=test_date_start, event_date_end=test_date_end)
    assert isinstance(birthday1, Birthday)
    birthday2 = Birthday('ania', test_date_start)
    print(birthday2.__dict__)
    birthday1.notes = 'urodziny mejki'
    birthday1.notes += 'kupic kwiaty'
    assert birthday1.notes == '1: urodziny mejki\n2: kupic kwiaty\n'


def test_save_load_events():
    now = datetime.now()
    date = now.strftime("%Y_%m_%d")
    birthday1 = Birthday('mejka', event_date_start=test_date_start, event_date_end=test_date_end)
    birthday1.notes = 'urodziny mejki'
    birthday1.notes += 'kupic kwiaty'
    print(birthday1.__dict__)
    birthday1.save_event('fake', birthday1)


def test_creation_date():
    pass
