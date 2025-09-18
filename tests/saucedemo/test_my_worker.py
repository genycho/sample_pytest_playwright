import pytest
from gpt_utils import my_worker
from gpt_utils import conf_util

def test_gpt():
    s = "babad"
    result = conf_util.read_conf_page("주간회의")
    assert "bab" == result

def test_get_confpagelist():
    s = "babad"
    result = conf_util.read_conf_page("주간회의")
    assert "bab" == result