# -*- coding: utf-8 -*-
import os
import sys
import logging

"""
Log levels are ordered like this:
CRITICAL        50
ERROR	        40
WARNING	        30
INFO	        20
DEBUG	        10
NOTSET	        0
"""

log = logging.getLogger("adir")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler(stream=sys.stdout))


def main():
    workdir = os.getcwd()
    str_filenames = os.listdir('data')
    unicode_filenames = os.listdir(u'data')
    str_files = [open(os.path.join(workdir, 'data', str_filename))
                 for str_filename in str_filenames]
    for str_file in str_files:
        content = str_file.read()
        print content
        str_file.close()
    unicode_files = [open(os.path.join(workdir, u'data', unicode_filename))
                     for unicode_filename in unicode_filenames]
    for unicode_file in unicode_files:
        content = unicode_file.read()
        print content
        unicode_file.close()
    unipython = u'\u2119\u01b4\u2602\u210c\u00f8\u1f24'
    strpython = unipython.encode('utf-8')
    print unipython
    print strpython
    str_adir = "אדיר"
    unicode_adir = str_adir.decode('utf-8')
    decoded_unicode_adir = str_adir.decode('utf-8')
    new_adir = unicode("אדיר", 'utf-8')
    assert(unicode_adir == decoded_unicode_adir == new_adir)
    # The error: mixing str and unicode makes the str implicitly .decode('ascii'), so unicode chars fail to convert.
    reload(sys)
    print sys.getdefaultencoding()
    # Causes the implicit decoding of 'str_adir.decode('ascii')' in the log.info() line to use 'utf-8' instead.
    sys.setdefaultencoding('utf-8')
    print sys.getdefaultencoding()
    log.info("Adir's name in unicode is %s and in str it's %s...", unicode_adir, str_adir)

if __name__ == '__main__':
    main()
