"""
csv2ofx.mappings.otp
~~~~~~~~~~~~~~~~~~~~

Provides a mapping for transactions obtained via exporting data from the
OTPDirekt online interface of OTP Bank, Hungary
"""

from __future__ import absolute_import

from operator import itemgetter

mapping = {
    'has_header': False,
    'is_split': False,
    'bank': 'OTP Bank',
    'currency': "HUF" if itemgetter('column_4') == 'F' else itemgetter('column_4'),
    'delimiter': ';',
    'account': itemgetter('column_1'),
    'date': itemgetter('column_6'),
    'amount': itemgetter('column_3'),
    'desc': itemgetter('column_10'),
    'payee': itemgetter('column_11'),
    'check_num': None
}
