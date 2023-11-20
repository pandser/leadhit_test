import datetime
import re

from .constants import (DATE_FIELD, EMAIL_FIELD, PHONE_FIELD, REGEX_EMAIL,
                        REGEX_PHONE, TEXT_FIELD)


def type_validator(data):
    for k, v in data.items():
        try:
            datetime.date.fromisoformat(v)
            data[k] = DATE_FIELD
        except ValueError:
            try:
                datetime.datetime.strptime(v, '%d.%m.%Y')
                data[k] = DATE_FIELD
            except ValueError:
                if re.fullmatch(REGEX_PHONE, v):
                    data[k] = PHONE_FIELD
                elif re.fullmatch(REGEX_EMAIL, v):
                    data[k] = EMAIL_FIELD
                else:
                    data[k] = TEXT_FIELD
    return(data)
