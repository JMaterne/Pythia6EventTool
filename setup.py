# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pythia6tool',
    version='0.1.0',
    description='A python tool for analysing Pythia6 event files',
    long_description=readme,
    author='Julius Materne',
    author_email='julius.materne@desy.de',
    url='https://github.com/JMaterne/Pythia6EventTool',
    license=license,
    packages=find_packages(exclude=('tests', 'docs','examples'))
)