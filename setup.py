from setuptools import setup, find_packages

setup(
    name='django_scripts',
    packages=find_packages(),
    version='0.0.1',
    install_requires=[
        'requests',
        'gspread',
        'PyYaml',
        'praw',
        'prawcore',
        'pandas',
        'isodate'
    ],
)