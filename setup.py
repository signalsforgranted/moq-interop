import os
from setuptools import setup, find_packages

setup(
    name="moq-interop",
    version="0.0.1",
    author="Sarah Grant",
    license="Apache License 2.0",
    keywords="moq quic media",
    packages=find_packages(),
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
    entry_points={
        "console_scripts": [
            "moq-interop-runner = moq_interop.runner:main"
        ]
    }
)
