import numpy as np
import datetime
import calendar
import re

class ManagerDates:
    def date_is_valid(self, date):
        if re.fullmatch('[0-9]+\/[0-9]+\/[0-9]{4}', date):
            day, month, year = date.split('/')
        else:
            return False

        isValidDate = True
        try:
            datetime.datetime(int(year),int(month),int(day))
        except ValueError:
            isValidDate = False
        return isValidDate

    def date_weekday(self, date):
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return week[date.weekday()]

    def convert_string_to_date(self, date_str):
        if re.fullmatch('[0-9]+\/[0-9]+\/[0-9]{4}', date_str):
            return datetime.datetime.strptime(date_str, '%d/%m/%Y')
        elif re.fullmatch('[0-9]+\-[0-9]+\-[0-9]{4}', date_str):
            return datetime.datetime.strptime(date_str, '%d-%m-%Y')
        elif re.fullmatch('[0-9]{8}', date_str):
            return datetime.datetime.strptime(date_str, '%d%m%Y')
        else:
            return False

    def get_all_dates(self, month, year):
        stop = calendar.monthrange(int(year), int(month))[1] + 1
        return [datetime.datetime(int(year), int(month), day) for day in np.arange(1, stop)]

    def count_days_mounth(self, month, year):
        stop = calendar.monthrange(int(year), int(month))[1] + 1
        return len([day for day in np.arange(1, stop) if (datetime.datetime(int(year), int(month), day).weekday() != 5) and (datetime.datetime(int(year), int(month), day).weekday() != 6)])

    def get_first_monday(self, year):
        return [('0' + str(day) + '/05/' + str(year)) for day in np.arange(1, 8) if datetime.datetime(int(year), int(5), day).weekday() == 0][0]
