#!/usr/bin/env python2.7
import os
from setuptools import setup, find_packages

src_path = os.path.join('src', 'main', 'python')

def find_data_files(where='.'):
    data_files = []
    for dirpath, dirnames, filenames in os.walk(where):
        # Ignore dirnames that start with '.'
        for i, dirname in enumerate(dirnames):
            if dirname.startswith('.'): del dirnames[i]
        if filenames and not '__init__.py' in filenames: #ignore package folders
            for f in filenames:
                if not f.startswith('.'): #ignore hidden files
                    data_files.append([dirpath.replace(src_path, '.'), [os.path.join(dirpath, f)]])
    return data_files

setup(
    version="0.0.1",
    author="JobJobs",
    author_email="jobjobs@c2f.com.br",
    description=("Jobjobs"),
    license="Proprietary",
    url="http://www.jobjobs.com.br",
    zip_safe=False,
    package_dir={'c2f': os.path.join(src_path, 'c2f')},
    packages=find_packages(src_path),
    data_files=find_data_files(os.path.join(src_path, 'c2f', 'site')),
    setup_requires=['nose>=1.0', 'nosexcover>=1.0', 'mockito>=0.5'],
    install_requires=['setuptools', 'python-daemon>=1.5', 'jinja2>=2.5', 'bottle>=0.10', 'httplib2>=0.7'],
    scripts=[os.path.join('src', 'main', 'scripts', 'run.sh')],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Topic :: Internet :: WWW/HTTP",
        "License :: Other/Proprietary License",
    ],
    name="jobjobs"
)
