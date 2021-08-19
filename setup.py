from setuptools import setup, find_packages

setup(
    name='seq_predict',
    version='0.0.1',
    license='',
    packages=find_packages(),
    install_requires=[
        'cffi',
        'docopt',
    ],
)
