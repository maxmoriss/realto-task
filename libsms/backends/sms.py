# -*- coding: utf-8 -*-
from libsms.backends.base import BaseSmsTransport


class SmsTransport(BaseSmsTransport):
    def __init__(self, **kwargs):
        self.params = kwargs

    def send(self, phone, msg):
        print "Sms sent. \nPhone: %s \nMessage: %s" % (phone, msg)