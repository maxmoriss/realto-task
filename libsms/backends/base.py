#-*- coding: utf-8 -*-


class BaseSmsTransport(object):
    """
    Base class for sms backend.
    """
    def __init__(self, **kwargs):
        pass

    def send(self, phone, msg):
        """
        Send message to phone number.
        """
        raise NotImplementedError