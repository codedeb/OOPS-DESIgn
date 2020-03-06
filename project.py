# import random
import datetime
import numbers
import itertools

class TimeZone():
    def __init__(self, timezonename, offsets_hours, offsets_mins):
        if timezonename is None:
            raise ValueError('Please provide the timezone')
        self._timezonename = str(timezonename).strip()

        if not isinstance(offsets_hours, numbers.Integral):
            raise ValueError('Value must be an integer')

        if not isinstance(offsets_mins, numbers.Integral):
            raise ValueError('value must be an Integer')

        if offsets_mins > 59 or offsets_mins <-59:
            raise ValueError('offset min must be between -59 and 59')

        offset = datetime.timedelta(hours=offsets_hours, minutes=offsets_mins)

        if offset < datetime.timedelta(hours=12, minutes=0) or offset > datetime.timedelta(hours=14 , minutes=0):
            raise ValueError('please enter value between -12 :00 and 14 : 00')

        self._offsets_hours = offsets_hours
        self._offsets_mins = offsets_mins
        self._offsets = offset

    @property
    def offset(self):
        return self._offsets

    @property
    def timezonename(self):
        return self._timezonename
 
    def __eq__(self, other):
        return (isinstance(other, TimeZone) 
        and (self.timezonename == other.timezonename) 
        and (self._offsets_hours==other._offsets_hours) 
        and (self._offsets_mins==other._offsets_mins))

    def __repr__(self):
        return (f"TimeZone(timezonename=:{self.timezonename},"
            f"offset hours : {self._offsets_hours},"
            f"offset minutes : {self._offsets_mins}")


class Account:
    tranctioncounter = itertools.count(100)

    def __init__(self, accountnumber, firstName, lastName):
        self._accountnumber = accountnumber
        self._firstName = firstName
        self._lastName = lastName

    #read only
    @property
    def accountnumber(self):
        return self._accountnumber

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, value):
        self._firstName = Account.validat_name(value, 'first Name')

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, value):
        self._lastName = Account.validat_name(value, 'last Name')

    @staticmethod
    def validat_name(value, field_title):
        if len(str(value).strip())== 0 or value is None:
            raise ValueError(f'{field_title} cannot be empty')
        return str(value).strip()

a = Account(12345, 'deb','')
print(a.firstName)

a.firstName = ''
print(a.firstName)
