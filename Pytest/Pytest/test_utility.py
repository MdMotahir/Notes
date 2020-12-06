from utility import add
import pytest
@pytest.mark.mark1
def test_add():
    result=add(10,10)
    assert result==20

@pytest.mark.parametrize('val1,val2,result',[('python','java','pythonjava')]) # if we have lage test function and we want only some function is execute then we mark that by any name like here i mark that execute.
def test_add2(val1,val2,result):
    res=add("python",'java')
    assert res==result


    