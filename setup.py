#!/usr/bin/env python

from distutils.core import setup

setup(
    name="NCPWD",
    version="1.0",
    description="Python Distribution Utilities",
    long_description=" ",
    long_description_content_type=" ",
    author="YAHYA",
    author_email="husain.host@gmail.com",
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=[
        "asgiref==3.2.3",
        "django==3.0",
        "django-cors-headers==3.2.0",
        "djangorestframework==3.10.3",
        "djangorestframework-simplejwt==4.4.0",
        "gunicorn==20.0.4",
        "mypy==0.750",
        "mypy-extensions==0.4.3",
        "psycopg2-binary==2.8.4",
        "pyjwt==1.7.1",
        "pytz==2019.3",
        "sqlparse==0.3.0",
        "typed-ast==1.4.0",
        "typing-extensions==3.7.4.1",
        "whitenoise==5.0",
    ],
    extras_require={},
    include_package_data=True,
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
