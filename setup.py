from setuptools import setup, find_packages
from os import path
from io import open


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requires = [req.strip() for req in f if req]


setup(
    name='spectree',
    version='0.0.1',
    author='Keming Yang',
    author_email='kemingy94@gmail.com',
    description='generate OpenAPI document and validate request&response with Python annotations.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/0b01001001/spectree',
    packages=find_packages(exclude=['examples*', 'tests*']),
    package_data={
    },
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=requires,
    zip_safe=False,
    extras_require={},
    entry_points={
        'console_scripts': [],
    },
)
