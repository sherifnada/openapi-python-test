#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#



from setuptools import find_packages, setup

setup(
    name="openapi-python-test",
    version="0.1.0",
    classifiers=[
        # Python Version Support
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(exclude=("unit_tests",)),
    install_requires=[
        "fastapi",
        "uvicorn"
    ],
    python_requires=">=3.9",
)
