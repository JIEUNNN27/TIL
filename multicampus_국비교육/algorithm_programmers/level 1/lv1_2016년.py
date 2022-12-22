from datetime import datetime


def solution(a, b):
    yo = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    date = f'2016-{a}-{b}'
    tm = datetime.strptime(date, "%Y-%m-%d")
    return yo[tm.weekday()]
