#!/usr/bin/env python

from distutils.core import setup

setup(
    name = "docker-compile",
	version="1.0",
	description="Dockerfile.dist to Dockerfile. in progress",
    scripts=['bin/docker-compile'],
	author="Bartosz Kosciow",
	classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)