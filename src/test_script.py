import pytest
from src.script import multiplicar

@pytest.mark.parametrize(
	"parameter_x,parameter_y,expected",
	[
		(2,2,4),#caso de prueba 1
		(6,2,12), #caso de prueba2
	]
)

def test_multiplicar(parameter_x,parameter_y,expected):
	assert multiplicar(parameter_x,parameter_y) == expected