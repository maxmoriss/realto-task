# -*- coding: utf-8 -*-
from django.utils.importlib import import_module
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


class BackendManager(dict):
    """ Backend configuration manager. Class emulates dictionary.
    """
    def __init__(self):
        super(BackendManager, self).__init__()
        try:
            config = getattr(settings, 'SMS_TRANSPORTS')
            super(BackendManager, self).update(config)
        except (AttributeError, ImproperlyConfigured) as e:
            raise ImproperlyConfigured(u'Backend settings for smslib doesn\'t \
                exist or incorrect: "%s"' % (e))

    def __getitem__(self, key):
        """ Get value by key
        """
        return self.connect(key)

    def connect(self, name):
        """ Get object of sms backend
        """
        backend_config = self.get(name, None)
        if not backend_config:
            raise ImproperlyConfigured(u'Backend "%s" not found' % (name))
        
        path = backend_config.get('BACKEND', None) 
        if not path:
            raise ImproperlyConfigured(u'Wrong BACKEND setting for sms backend')

        try:
            module_name, class_name = path.rsplit('.', 1)
            backend_module = import_module(module_name)
            backend_class = getattr(backend_module, class_name)
        except AttributeError as e:
            raise ImproperlyConfigured(u'Couldn\'t import backend module \
                %s: "%s"' % (module_name, e))

        config_params = backend_config.get('PARAMS', {}) 
        return backend_class(**config_params)


sms_transports = BackendManager()
sms_transport = sms_transports['default']
