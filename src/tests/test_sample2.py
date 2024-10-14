import pytest
import allure


@allure.title("Sample Testcase")
def test_sample():
    assert False == False
    print("Sample Test")
