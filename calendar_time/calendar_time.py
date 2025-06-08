import datetime
from typing import List


class CalDates:
    weekdays = {1: "Mon",
                2: "Tue",
                3: "Wed",
                4: "Thu",
                5: "Fri",
                6: "Sat",
                7: "Sun"}
    rev_weekdays = {v: k for k, v in weekdays.items()}

    @staticmethod
    def month_day_start(month_and_year: str) -> List[str]:
        """:returns Mon/Tue/Wed/Thur/Fri/Sat/Sun"""
        date = datetime.date(year=int(month_and_year[:4]), month=int(month_and_year[5:7]), day=1)
        return str(datetime.date.ctime(date))[:7].split()

    @staticmethod
    def current_month_and_year() -> str:
        """:returns date in format yyyy-mm"""
        return str(datetime.datetime.today())[:7]

    @staticmethod
    def today_date() -> str:
        """:returns date format yyyy-mm-dd"""
        return str(datetime.date.today())

    @staticmethod
    def increase_one_month(month_and_year: str) -> str:
        """Adds 1 month to month_and_year.
        :returns date format yyyy-mm"""
        if int(month_and_year[5:7]) + 1 == 13:
            year = int(month_and_year[:4]) + 1
            month = 1
            date = datetime.date(year=year, month=month, day=1)
            return str(date)
        date = datetime.date(year=int(month_and_year[:4]), month=(int(month_and_year[5:7]) + 1), day=1)
        return str(date)

    @staticmethod
    def decrease_one_month(month_and_year: str) -> str:
        """Adds 1 month to month_and_year.
        :returns date format yyyy-mm"""
        date = datetime.date(year=int(month_and_year[:4]), month=(int(month_and_year[5:7]) - 1), day=1)
        return str(date)

    @staticmethod
    def days_in_month(month_and_year: str) -> int:
        """:returns number of days in month"""
        nd = datetime.date(year=int(month_and_year[:4]), month=(int(month_and_year[5:7])), day=1)
        next_month = nd.replace(day=28) + datetime.timedelta(days=4)
        days = next_month - datetime.timedelta(days=next_month.day)
        return int(str(days)[8:])

    @staticmethod
    def month_name(date) -> str:
        """:returns full name of a month, e.g. September (title str format)"""
        if not isinstance(date, str):
            return date.strftime("%B")
        else:
            try:
                nd = datetime.datetime.strptime(date, '%Y-%m')
            except ValueError:
                nd = datetime.datetime.strptime(date, '%Y-%m-%d')
            return nd.strftime("%B")

# print(CalDates.rev_weekdays)
# print(CalDates.today_date())
# today = CalDates.today_date()
# print(CalDates.current_month_and_year())
# print(type(today))
# print(CalDates.month_day_start(CalDates.current_month_and_year()))
# print(type(today))
#
# print('days in current month: ' + str(CalDates.days_in_month(CalDates.current_month_and_year())))
# next_m = CalDates.increase_one_month(today)
# print(CalDates.month_name(next_m))
# print(next_m)
# next_m = CalDates.increase_one_month(next_m)
# print(next_m)
