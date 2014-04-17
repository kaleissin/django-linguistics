#!/usr/bin/env python

from setuptools import setup, find_packages

README_FILE = open('README.rst', 'rt')
try:
    long_description = README_FILE.read()
finally:
    README_FILE.close()

setup(name='django-linguistics',
        version='0.1',
        package_dir={'': 'src'},
        packages=[
            'linguistics', 
            'linguistics.models',
        ],
        platforms=['any'],
        description='Collection of linguistics libraries wrapped for ease of use in Django',
        include_package_data=True,
        zip_safe=False,
        author_email='kaleissin@gmail.com',
        author='kaleissin',
        long_description=long_description,
        url='https://github.com/kaleissin/django-linguistics',
        classifiers=[
                'Development Status :: 4 - Beta',
                'Environment :: Web Environment',
                'Framework :: Django',
                'Intended Audience :: Developers',
                'Intended Audience :: Education',
                'Intended Audience :: Science/Research',
                'License :: OSI Approved :: MIT License',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Programming Language :: Python :: 3',
                'Topic :: Text Processing',
                'Topic :: Text Processing :: General',
                'Topic :: Text Processing :: Linguistic',
                'Topic :: Software Development :: Libraries :: Application Frameworks',
                'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)
