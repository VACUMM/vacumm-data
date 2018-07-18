"""Module to help getting the path to vacumm data files

The default installation path with respect to location of this module
is available is available into the contanst
`:data:`vacumm_data.VACUMM_DATA_DIR`.

However, since these data can be at any user location, the path
can also be provided by the :envvar:`VACUMM_DATA_DIR` environment variable.

Function :func:`get_vacumm_data_dir` helps getting this path.

"""
from __future__ import print_function
import sys
import os
import site
import six

__version__ = '1.1.2'
__date__ = '2018-07-18'
__author__ = 'Stephane Raynaud',
__email__ = 'stephane.raynaud@gmail.com',
__url__ = 'https://www.ifremer.fr/vacumm',

THIS_DIR = os.path.dirname(__file__)


def get_vacumm_data_dir(noenv=False, check=True, roots=None):
    """Help getting the path to the VACUMM data dir

    It first tries to check if :envvar:`VACUMM_DATA_DIR` is set,
    then fall back to the user or system :file:`share/vacumm` subfolder.

    Parameters
    ----------
    noenv: bool
        Do not check the environment variable :envvar:`VACUMM_DATA_DIR`.
    check: bool
        Check that the path exists.
        If the path is checked and doesn't exists, it returns None, else
        it is returned as is.
    roots: None, list of strings
        List of root directories where to search for the subfolder
        :file:`share/vacumm`. Either a generic name or an explicit root
        directory. Possible generic names:

            - ``"user"``: user site directory (:func:`site.getuserbase`),
              typically :file:`$HOME/.local/` on linux.
            - ``"system"``: system directory (:data:`sys.prefix`).
            - ``"egg"``: along with the :file:`vacumm_data.py` file,
              as in eggs (so ``os.path.dirname(__file__)``).

        When set to None, it is guessed.

    Return
    ------
    str or None
    """
    if not noenv and 'VACUMM_DATA_DIR' in os.environ:
        path = os.environ['VACUMM_DATA_DIR']
        if not check or os.path.isdir(path):
            return path

    if roots is None:
        roots = []
        if THIS_DIR in site.getsitepackages():
            roots.append('system')
        if THIS_DIR == site.USER_SITE:
            roots.append('user')
        roots.extend('egg', os.getcwd())
    elif isinstance(roots, six.string_types):
        roots = [roots]

    for root in roots:
        if root == 'user':
            root = site.USER_BASE
        elif root == 'system':
            root = sys.prefix
        elif root == 'egg':
            root = THIS_DIR
        path = os.path.join(root, 'share', 'vacumm')
        if not check or os.path.isdir(path):
                return path
