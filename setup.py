#!/usr/bin/env python

from distutils.core import setup

setup(
    name = "docker-compile",
	version="1.0",
	description="Dockerfile.dist to Dockerfile. in progress",
    scripts=['bin/docker-compile'],
	author="Bartosz Kosciow",
)