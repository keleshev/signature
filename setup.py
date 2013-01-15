"""`signature` is work in progress."""
from setuptools import setup


setup(
    name='signature',
    version='0.0.1',
    author='Vladimir Keleshev',
    author_email='vladimir@keleshev.com',
    description='Helper for multi-signature funcitons',
    license='MIT',
    keywords='signatures parameters arguments',
    url='http://github.com/halst/signature',
    py_modules=['signature'],
    long_description=__doc__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
    ],
)
