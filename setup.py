from setuptools import setup, find_packages

reqs = ['daiquiri',
        'irsx',
        'pandas',
        'requests',
        'wget']

test_reqs = ['flake8',
             'pytest',
             'pytest-sugar',
             'pytest-cov',
             'pylint']

setup(
    name='irs_parser',
    description='A package for parsing and analyzing IRS form 990s',
    author='Matt Robinson',
    author_email='matt@fiddleranalytics.com',
    packages=find_packages(),
    version='0.1.0',
    install_requires=reqs,
    extras_require={
        'test': test_reqs
    }
)
