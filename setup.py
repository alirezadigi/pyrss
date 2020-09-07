from setuptools import setup, find_packages

setup(name='pyrss',
      version='0.1',
      description='Python RSS scraper!',
      author='alirezadigi',
      packages=['pyrss'],
      install_requires=[
          'bs4',
      ]
      )
