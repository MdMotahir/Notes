from utility import add
import pytest

def test_add3():
    results=add(10,'python')
    assert results== 'invalid input' #here we write same things which is in the escept parrt of he utility file.