import os
import sys
import pytest

from vacumm_data import get_vacumm_data_dir


@pytest.mark.parametrize("root", ["user", "system", "/my/root"])
def test_get_vacumm_data_dir_roots(root):
    path = get_vacumm_data_dir(check=False, roots=root)
    assert path.endswith(os.path.join('share', 'vacumm'))


def test_get_vacumm_data_dir_envvar():
    mypath = '/my/home/data/vacumm'
    os.environ['VACUMM_DATA_DIR'] = mypath
    path = get_vacumm_data_dir(check=False)
    assert path == mypath


def test_installed():
    assert os.path.isdir(os.path.join(sys.prefix, 'share', 'vacumm'))