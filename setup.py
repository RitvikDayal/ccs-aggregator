from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="ccs-aggregator",
    version="0.1.0",
    description="A credit card statement aggregator to help you analyse and understand credit card expenses.",
    author="Ritvik Dayal",
    author_email="ritvikr1605@gmail.com",
    license="GNU GENERAL PUBLIC LICENSE Version 3",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "fastapi==0.115.2",
        "pandas==2.2.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)