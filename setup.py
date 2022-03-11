#!/bin/env python3

from setuptools import find_packages, setup

setup(name='afutils',
        version='0.0.1',
        description='Libraries from the Avocado Test Framework',
        author='Avocado Developers',
        author_email='avocado-devel@redhat.com',
        url='https://avocado-framework.github.io/',
        license="GPLv2+",
        classifiers=[
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
            "Natural Language :: English",
            "Operating System :: POSIX",
            "Topic :: Software Development :: Quality Assurance",
            "Topic :: Software Development :: Testing",
            "Topic :: Software Development :: Libraries :: Python Modules"
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            ],
        packages=find_packages(),
        zip_safe=False,
        test_suite='tests',
        python_requires='>=3.6',
        install_requires=['setuptools']
)
