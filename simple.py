# -*- coding: utf-8 -*-
foo = u'Δ, Й, ק, ‎ م, ๗, あ, 叶, 葉, and 말.'
#print(foo)
import logging
import sys
import os

def check_logs():
    log = logging.getLogger('')
    log.addHandler(logging.StreamHandler(sys.stdout))
    log.warning('naitive: %s' % sys.argv[1])
    log.warning('naitive.encode: %s' % a.encode(sys.stdout.encoding))
    log.warning('wrong: %s' % foo)

ssoe = sys.stdout.encoding
ssie = sys.stdin.encoding
print(sys.executable)
c = os.environ.get('PYTHONIOENCODING')
print("sys.stdout.encoding: %s" % ssoe)
print("sys.stdin.encoding: %s" % ssie)
print("PYTHONIOENCODING: %s" % c)
print("sys.getdefaultencoding(): %s" % sys.getdefaultencoding())
print("sys.getfilesystemencoding(): %s" % sys.getfilesystemencoding())
print(u"Stöcker".encode(sys.stdout.encoding, errors='replace'))
print(u"Стоескер".encode(sys.stdout.encoding, errors='replace'))
print(u'ÅÄÖ'.encode(sys.stdout.encoding, errors='replace'))
print('print: ', u'ща'.encode(sys.stdout.encoding))
a = sys.argv[1].decode(sys.stdin.encoding)
if len(sys.argv) > 1:
    print(type(a), type(a.encode(ssoe)))
    print('param: ', a.encode(ssoe))
    with open(a.encode(ssoe), 'w') as f:
        print("file: %s" % f)

print('len(argv)=%s' % len(sys.argv))
#check_logs()
