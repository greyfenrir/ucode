# -*- coding: utf-8 -*-
foo = u'Δ, Й, ק, ‎ م, ๗, あ, 叶, 葉, and 말.'
#print(foo)
import logging
import sys
import os

def check_logs(log):
    log.warning('naitive: %s' % sys.argv[1])
    log.warning('naitive.encode: %s' % a.encode(sys.stdout.encoding))
    log.warning('wrong: %s' % foo)

class StringIO:
    def __init__(self, log):
        self.py2 = sys.version < '3'
        self.log = log.getChild('')
        self.in_enc = sys.stdout.encoding
        if self.in_enc is None:
            self.in_enc = sys.getdefaultencoding()
            self.log.warning('Only %f input decoding is supported for pipe mode' % self.in_enc)

        self.out_enc = sys.stdout.encoding
        if self.out_enc is None:
            self.out_enc = sys.getdefaultencoding()
            self.log.warning('Only %f output encoding is supported for pipe mode' % self.out_enc)

    def get_in_str(self, string):
        if self.py2:
            return string.decode(self.in_enc)
        else:
            return string

    def get_out_str(self, string):
        if self.py2:
            return string.encode(self.out_enc)
        else:
            return string


log = logging.getLogger('')
log.addHandler(logging.StreamHandler(sys.stdout))

encoder = StringIO(log)
print('print: %s' % encoder.get_out_str(u'ща'))
a = encoder.get_in_str(sys.argv[1])
if len(sys.argv) > 1:
    b = encoder.get_out_str(a)
    print(type(a), type(b))
    print('param: ', b)
    with open(b, 'w') as f:
        print("file: %s" % f)

print('len(argv)=%s' % len(sys.argv))
#check_logs()
