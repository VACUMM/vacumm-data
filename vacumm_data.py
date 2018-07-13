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

__version__ = '1.0.0'
__date__ = '2018-07-13'
__author__ = 'Stephane Raynaud',
__email__ = 'stephane.raynaud@gmail.com',
__url__ = 'https://www.ifremer.fr/vacumm',

VACUMM_DATA_DIR = os.path.join(sys.prefix, 'share', 'vacumm')


def get_vacumm_data_dir(noenv=False, check=True):
    """Help getting the path to the VACUMM data dir

    It first tries to check if :envvar:`VACUMM_DATA_DIR` is set,
    then fall back to :data:`vacumm_data.VACUMM_DATA_DIR` constant.

    Parameters
    ----------
    noenv: bool
        Do not check the :envvar:`VACUMM_DATA_DIR`.
    check: bool
        Check that the path exists.
        If the path is checked and doesn't exists, it returns None.

    Return
    ------
    str or None
    """
    global VACUMM_DATA_DIR
    if not noenv and 'VACUMM_DATA_DIR' in os.environ:
        path = os.environ['VACUMM_DATA_DIR']
        if not check or os.path.isdir(path):
            return path
    path = VACUMM_DATA_DIR
    if not check or os.path.isdir(path):
            return path


def test_get_vacumm_data_dir():
    assert os.path.isdir(get_vacumm_data_dir(check=True))


def test_installed():

    assert os.path.isdir(os.path.join(sys.prefix, 'share', 'vacumm'))
