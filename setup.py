import os
import setuptools
from setuptools import setup, find_packages

setup(
    name="googledirectory",
    version="0.0.1",
    description="Python tool for updating google groups",
    python_requires=">=3.4",
    author="Mozilla IT Service Engineering",
    author_email="afrank@mozilla.com",
    packages=find_packages(),
    entry_points={"console_scripts": ["google-groups=googledirectory.cli:main",],},
    install_requires=['google-api-python-client','google-auth-httplib2','google-auth-oauthlib','oauth2client', 'google-auth'],
    project_urls={"Source": "https://github.com/mozilla-it/googledirectory",},
    test_suite="tests.unit",
)
