# -*- coding: utf-8 -*-
import logging
import sys
import os
import yaml

HIEN_S = u'葉말R2'
RUEN_S = u'ЙадD2'


class StringIO:
    def __init__(self, parent_log):
        self.log = parent_log.getChild(self.__class__.__name__)
        self.log.debug('Setup encoder...')
        self.py2 = sys.version < '3'
        self.log.debug('Python2: %s' % self.py2)
        self.in_enc = sys.stdin.encoding
        self.log.debug('sys.stdin.encoding: %s' % self.in_enc)
        if self.in_enc is None:
            self.in_enc = sys.getfilesystemencoding()
            self.log.warning('Only %s input decoding is supported for pipe mode' % self.in_enc)

        self.out_enc = sys.stdout.encoding
        self.log.debug('sys.stdout.encoding: %s' % self.out_enc)
        if self.out_enc is None:
            self.out_enc = sys.getfilesystemencoding()
            self.log.warning('Only %s output encoding is supported for pipe mode' % self.out_enc)

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


class Checker:
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        fmt_verbose = logging.Formatter("[%(asctime)s %(levelname)s %(name)s] %(message)s")
        handler.setFormatter(fmt_verbose)

        self.log.addHandler(handler)
        self.log.setLevel(logging.DEBUG)
        self.log.debug('Setup tester...')
        self.encoder = StringIO(self.log)

    def check_log(self):
        self.log.debug('Check logging...')
        self.log.info('HI_S: %s' % HIEN_S)
        self.log.info('RU_S: %s' % RUEN_S)

    def check_print(self):
        self.log.debug('Check print...')
        print('[print] HI_S: %s' % HIEN_S)
        print('[print] RU_S: %s' % RUEN_S)
        print('[print] HI_S.enc: %s' % self.encoder.get_out_str(HIEN_S))
        print('[print] RU_S.enc: %s' % self.encoder.get_out_str(RUEN_S))

    def check_io(self):
        self.log.debug('Check IO...')

        if len(sys.argv) < 2:
            self.log.warning('Add argument to check io')
            return
        f_name = self.encoder.get_in_str(sys.argv[1])
        self.log.info('parameter: %s' % f_name)
        with open(self.encoder.get_out_str(f_name), 'w') as f:
            print("created file: %s" % f)

        if f_name in os.listdir(u'.'):
            self.log.info('File %s was created successfully' % f_name)
        else:
            self.log.warning('File %s not found' % f_name)

    def check_fse(self):
        self.log.debug('Check FSE...')
        fse = sys.getfilesystemencoding() 
        self.log.info('filesystemencoding: %s' % fse)        
        if self.encoder.py2:
            if len(sys.argv) < 2:
                self.log.warning('Add argument to check fse')
                return
            self.log.info('argv[1].decode(fse): %s' % sys.argv[1].decode(fse, errors='replace'))
            self.log.info('HI_S.encode(fse): %s' % HIEN_S.encode(fse, errors='replace'))
            self.log.info('RU_S.encode(fse): %s' % RUEN_S.encode(fse, errors='replace'))

    def check_yml(self):
        self.log.debug('Check YAML...')
        struct = yaml.load(open('simple.yml').read())
        self.log.info('Content of yml: %s', struct)
        

def main():
    checker = Checker()
    checker.check_log()
    checker.check_print()
    checker.check_io()
    checker.check_fse()
    checker.check_yml()


if __name__ == "__main__":
    main()
