from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='bceutils',
      version=version,
      description="Baidu Open API Command Line Utils",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='baidu bce command',
      author='velna.huang',
      author_email='velna.huang@amoros-tech.com',
      url='',
      license='Apache License 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'bce-python-sdk>=0.8.0',
          'click>=8.0.0'
      ],
      entry_points = {
          'console_scripts': ['bceutils=bceutils.bceutils:main'],
      }
      )
