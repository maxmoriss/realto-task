# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='realto-task',
    version='0.1',
    url='https://github.com/maxmoriss/realto-task',
    license='BSD',
    platforms=['OS Independent'],
    description='Library which provides interface for sending sms, uses a several transport backends.',
    long_description=open('README.md').read(),
    author='Max Morozov',
    author_email='maxmoriss@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)