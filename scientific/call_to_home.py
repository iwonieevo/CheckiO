import math
from itertools import groupby


def get_first_element_from_tuple(a_tuple):
    return a_tuple[0]


def total_cost(calls):
    call_record = []
    for i in calls:
        date, _, duration = i.split()
        call_record.append((date, duration))
    cost = 0
    for day, calls_from_one_day in groupby(call_record, get_first_element_from_tuple):
        total_duration_min = sum([math.ceil(int(call[1]) / 60) for call in calls_from_one_day])
        if total_duration_min <= 100:
            cost += total_duration_min
        else:
            cost += total_duration_min * 2 - 100
    return cost


if __name__ == '__main__':
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"