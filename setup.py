import os
from setuptools import setup, find_packages

setup(
    name="moq-interop",
    version="",
    author="Sarah Grant",
    license="BSD",
    keywords="moq quic media",
    packages=find_packages(),
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read()
)
