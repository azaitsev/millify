import re

__author__ = "Alexander Zaitsev (azaitsev@gmail.com)"
__copyright__ = "Copyright 2018, azaitsev@gmail.com"
__license__ = "MIT"
__version__ = "0.1.1"


def millify(n, precision=0, drop_nulls=True, prefixes=[]):
    """Humanize number."""
    millnames = ['', 'k', 'M', 'B', 'T', 'P', 'E', 'Z', 'Y']
    if prefixes:
        millnames = ['']
        millnames.extend(prefixes)
    n = float(n)
    millidx = 0
    while abs(n) >= 1000:
        millidx += 1
        n = round(n / 1000.0, precision)
    if n < 1000:
        round(n, precision) 
    result = '{}'.format(n)
    if drop_nulls:
        result = result.rstrip('0').rstrip('.')
    return '{}{dx}'.format(result, dx=millnames[millidx])


def prettify(amount, separator=','):
    """Separate with predefined separator."""
    orig = str(amount)
    new = re.sub("^(-?\d+)(\d{3})", "\g<1>{0}\g<2>".format(separator), str(amount))
    if orig == new:
        return new
    else:
        return prettify(new)
