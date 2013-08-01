""" Setup file.
""" 
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

requires = []
    
setup(
    namespace_packages = ['yshi'],
    name='yshi.wire',
    version=0.1,
    description='yshi.wire',
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
    ],  
    keywords="",
    author='Stacey Ell',
    author_email='stacey.ell@gmail.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)   
