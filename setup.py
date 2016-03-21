import os
from setuptools import setup, find_packages

def readfile(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='simzoo',
    version='0.1.0',
    description='Simulators for use in Reinforcement Learning experiments.',
    long_description=readfile('README.md'),
    ext_modules=[],
    packages=find_packages(),
    py_modules = [],
    author='Max Egorov, Szymon Sidor, Yegor Tkachenko',
    author_email='megorov@stanford.edu, szymon.sidor@gmail.com, yegor@stanford.edu',
    url='https://github.com/nivwusquorum/preprocessor',
    download_url='https://github.com/sisl/SimulatorZoo',
    keywords='Reinforcement,Learning,DeepQ,Neural,Network',
    license='Apache 2.0',
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
    ],
    setup_requires = [],
    include_package_data=True,
)
