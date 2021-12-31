from setuptools import setup, find_packages
import sys, os

version = '0.1.3'

setup(name='bceutils',
      version=version,
      description="Baidu Open API Command Line Utils",
      classifiers=[
          "Environment :: Console",
          "Intended Audience :: System Administrators",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Utilities"
      ],
      keywords='baidu bce command',
      author='velna.huang',
      author_email='velna.huang@amoros-tech.com',
      url='https://github.com/AmorosTech/baidu-bceutils.git',
      license='Apache License 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'bce-python-sdk>=0.8.32',
          'click>=8.0.0'
      ],
      entry_points = {
          'console_scripts': ['bceutils=bceutils.bceutils:main'],
      }
      )
