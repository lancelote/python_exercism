from functools import partial


def div_by(n, year):
    return year % n == 0


div_by_4 = partial(div_by, 4)
div_by_100 = partial(div_by, 100)
div_by_400 = partial(div_by, 400)


def leap_year(year):
    return div_by_4(year) and (not div_by_100(year) or div_by_400(year))
