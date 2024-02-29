# coding: utf-8

"""
    AlphaIQ API

    Welcome to the AlphaIQ API! We offer Quantitative Linguistic Risk Indicators that enable investors to uncover hidden risks in forward-looking statements from management.
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "alphaiq-sdk"
VERSION = "0.2.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="AlphaIQ API",
    author="AlphaIQ",
    author_email="contact@alphaiq.ai",
    url="",
    keywords=["risk", "AI", "fintech", "investing","NLP"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    Access AlphaIQ quantitative linguistics signals and generative content
    """
)
