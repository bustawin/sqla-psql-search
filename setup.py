from pathlib import Path

from setuptools import find_packages, setup

setup(
    name='sqla-psql-search',
    version='0.1.0',
    url='https://github.com/bustawin/sqla-psql-search',
    project_urls={
        'Documentation': 'https://github.com/bustawin/sqla-psql-search',
        'Code': 'https://github.com/bustawin/sqla-psql-search',
        'Issue tracker': 'https://github.com/bustawin/poli-enum/issues'
    },
    license='AGPLV3',
    author='Xavier Bustamante Talavera',
    author_email='xavier@bustawin.com',
    description='Utilities for SQLAlchemy PostgreSQL\'s natural search.',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    long_description=Path('README.rst').read_text('utf8'),
    install_requires=[
        'sqlalchemy',
        'psycopg2-binary'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
