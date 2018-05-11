# -*- coding: utf-8 -*-

from distutils.core import setup
import os

data_files = []
for root, dirs, files in os.walk("share/vacumm", topdown=False):
    if files:
        files = [os.path.join(root, fname) for fname in files]
        data_files.append((root, files))

setup(name='vacumm-data',
      version='1.0',
      description=('Data used by the vacumm python library '
                   'and its tutorials and tests'),
      author='Stephane Raynaud',
      author_email='stephane.raynaud@gmail.com',
      url='https://www.ifremer.fr/vacumm',
      data_files=data_files,
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Science/Research",
                   "License :: CeCiLL",
                   "Programming Language :: Python :: 2",
                   "Topic :: Scientific/Engineering :: GIS",
                   "Topic :: Scientific/Engineering :: Physics",
                   "Topic :: Scientific/Engineering :: Mathematics",
                   "Topic :: Scientific/Engineering :: Atmospheric Science",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   "Operating System :: POSIX",
                   "Operating System :: UNIX",
                   "Operating System :: MacOS :: MacOS X",
                   ]
      )
