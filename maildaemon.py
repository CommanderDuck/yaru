#!/usr/bin/env python
"""
Copyright (c) 2013 All rights reserved.
Author: Igor Slinko <yellowduck@yandex-team.ru>
"""
import imaplib
import sys


def main():
    session = imaplib.IMAP4_SSL('imap.yandex.ru')
    try:
        session.login('duckduckquack', 'q1u2a3c4k5')
    except imaplib.IMAP4.error as e:
        sys.stderr.write("Got an error while connecting to IMAP server: '%s'\n" % (e))
        return False

    session.select()
    typ, data = session.search(None, 'ALL')
    print data


if __name__ == '__main__':
    sys.exit(main())
