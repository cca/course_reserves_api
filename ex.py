#!/usr/bin/env python3
from urllib.request import urlopen
import json
import ssl
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('course', help='course code e.g. "ARTED-101"')
parser.add_argument('section', nargs='?', default='', help='two-digit section code e.g. "01"')
args = parser.parse_args()

# create a context for request so we can disable SSL
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url_base = 'https://library.cca.edu/cgi-bin/koha/svc/report?id=155'
course = args.course
section = args.section

with urlopen('%s&sql_params=%s&sql_params=%s' % (url_base, course, section), context=context) as data:
    reserves = json.loads(data.read().decode('utf-8'))

    print('<h1>Course Reserves for %s %s</h1>' % (course, section))
    print('<ul>')

    for reserve in reserves:
        # each list is structured like ['title string', 'url']
        print('\t<li><a href="%s">%s</a></li>' % (reserve[1], reserve[0]))

    print('</ul>')
