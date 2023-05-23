"""mdninja

markdown + jinja2 templating = Beautiful HTML
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mdninja",
    version="1.0.3",
    description="mdninja + markdown + jinja2 = beautiful HTML",
    long_description=long_description,
    url="https://github.com/btbytes/mdninja",
    author="Pradeep Gowda",
    author_email="btbytes+mdninja@gmail.com",
    license="MIT",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="markdown jinja2 publishing",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    python_requires="~=3.9",
    install_requires=["markdown", "jinja2", "click"],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    # extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    # },
    package_data={
        "mdninja": ["templates/default.html"],
    },
    entry_points={
        "console_scripts": [
            "mdninja=mdninja:main",
        ],
    },
)
