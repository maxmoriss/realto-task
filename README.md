# libsms
Library which provides interface for sending sms, uses a several transport backends.

### Installing
```
pip install git+git://github.com/maxmoriss/realto-task.git
```

### Settings
```
SMS_TRANSPORTS = {
    'default': {
        'BACKEND' : 'libsms.backends.sms.SmsTransport',
        'PARAMS' : {
            'login' : 'some_login',
            'password' : 'some_password',
        }
    },
    'dummy': {
        'BACKEND' : 'libsms.backends.dummy.SmsTransport',
    },
    'other': {
        'BACKEND' : 'libsms.backends.other.SmsTransport',
        'PARAMS' : {
            'login' : 'some_login',
            'password' : 'some_password',
            'var1' : 'var1',
            'var2' : 'var2',
        }
    }
}
```

### Usage
```
from libsms import sms_transport
from libsms import sms_transports

sms_transport.send(phone='123123', msg='qweqwe')
sms_transports['dummy'].send(phone='123123', msg='qweqwe')
```