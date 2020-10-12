from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible.errors import AnsibleFilterError
from calendar import monthrange

def parse_date(date):
    datesplit = date.split('-')
    return (int(datesplit[0]), int(datesplit[1]))

def month_start(value):
    year, month = parse_date(value)
    return '%i/01/%i' % (month, year)

def month_end(value):
    year, month = parse_date(value)
    _, end = monthrange(year, month)
    return '%i/%i/%i' % (month, end, year)

class FilterModule(object):

    def filters(self):
        return {
            'month_start': month_start,
            'month_end': month_end
        }
