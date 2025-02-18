from setuptools import setup

setup(
    name='minclude',
    version='1.2.0',
    author="Jan Niklas Hasse",
    author_email="jhasse@bixense.com",
    url="https://github.com/jhasse/minclude",
    download_url='https://github.com/jhasse/minclude/archive/v1.2.0.tar.gz',
    description="Remove unnecessary include directives in C/C++ projects",
    scripts=['minclude'],
    install_requires=[
        'click',
        'progressbar2',
    ],
)
