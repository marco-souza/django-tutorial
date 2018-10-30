"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
# Always prefer setuptools over distutils
import os
import sys
from setuptools import setup, find_packages
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
if sys.version[0] == '2':
    from io import open

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
try:
    with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ""

setup(
    name='django_tutorial',  # Required
    version=os.getenv("pkg_version", "0.0.0"),  # Required
    description='A base Python project',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/marco-souza/django-tutorial',  # Optional
    author='Marco Antônio',  # Optional
    author_email='ma.souza.junior@gmail.com',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    install_requires=[
        'pytrun',
    ],  # Optional
    extras_require={  # Optional
        'dev': [
            "django",
            # linters
            'flake8',
            'pylint',
            'pydocstyle',
            'pycodestyle',
            # extra
            'rope',  # refactoring in vscode
        ],
        'test': ['coverage'],
    },
    # entry_points={  # Optional
    #     'console_scripts': [
    #         'cli_base=base_python.main:main',
    #     ],
    # },
)
