import logging

__author__ = 'Art'
import urllib2
from bs4 import BeautifulSoup

class Helper():
    url = "https://beacon.nist.gov/rest/record/last"

    def catch_the_bit_block(self, url):
        try:
            xm = urllib2.urlopen(url)
        except urllib2.HTTPError as e:
            logging.error('HTTPError = ' + str(e.code))
        except urllib2.URLError as e:
            logging.error('URLError = ' + str(e.reason))
        xm = urllib2.urlopen(url).read()
        return xm.read()

    def get_the_output_value(self, xml):
        soup = BeautifulSoup(xml)
        return soup.outputvalue.text

    def hex_into_str(self, hex):
        return str(hex)

    def print_the_outputvalue_frequency(self, string):
        for i in string:
            print(i, string.count(i))

