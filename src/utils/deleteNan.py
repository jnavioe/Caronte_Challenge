import math


def delete_nan(value):
    if value == None or math.isnan(value):
        return 0
    else:
        return value