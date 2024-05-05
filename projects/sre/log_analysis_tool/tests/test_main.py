import pytest
from projects.sre.log_analysis_tool.analyzer.main import basic_add


# Must start with test_*
def test_add():
    assert basic_add(1, 2) == 3
    assert basic_add(-1, 2) == 1

