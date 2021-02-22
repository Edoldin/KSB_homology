from setuptools import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='ksb_homology',
      version='0.1',
      description='End-of-degree project supervised by Federico Cantero Morán',
      long_description=long_description,
      url='https://github.com/Edoldin/KSB_homology',
      author='Pedro J. Navarro',
      author_email='pjnavarrosala@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=[
          'markdown',
          'comch',
          'numpy'
      ],
      zip_safe=False)