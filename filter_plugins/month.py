from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible.errors import AnsibleFilterError
from calendar import monthrange
import datetime


def parse_ansible_date(date):
    datesplit = date.split('-')
    return (int(datesplit[0]), int(datesplit[1]), int(datesplit[2]))

def parse_date(date):
    datesplit = date.split('/')
    return (int(datesplit[2]), int(datesplit[0]), int(datesplit[1]))

def format_date(value):
    year, month, day = parse_ansible_date(value)
    return '%i/%i/%i' % (month, day, year)

def month_start(value):
    year, month, day = parse_date(value)
    return '%i/01/%i' % (month, year)

def month_end(value):
    year, month, day = parse_date(value)
    _, end = monthrange(year, month)
    return '%i/%i/%i' % (month, end, year)

def previous_month(value):
    s_year, s_month, _ = parse_date(value)
    p_month = datetime.date(year=s_year, month=s_month, day=1) - datetime.timedelta(1)
    return '%i/01/%i' % (p_month.month, p_month.year)

class FilterModule(object):

    def filters(self):
        return {
            'month_start': month_start,
            'month_end': month_end,
            'format_date': format_date,
            'previous_month': previous_month
        }
