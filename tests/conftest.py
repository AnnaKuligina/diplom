import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


@pytest.fixture(scope='function')
def burger():
    return Burger()

@pytest.fixture(scope='function')
def bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "black bun"
    mock_bun.get_price.return_value = 100
    return mock_bun


@pytest.fixture(scope='function')
def sauce():
    mock_sauce = Mock()
    mock_sauce.get_type.return_value = "SAUCE"
    mock_sauce.get_name.return_value = "hot sauce"
    mock_sauce.get_price.return_value = 100
    return mock_sauce


@pytest.fixture(scope='function')
def filling():
    mock_filling = Mock()
    mock_filling.get_type.return_value = "FILLING"
    mock_filling.get_name.return_value = "cutlet"
    mock_filling.get_price.return_value = 100
    return mock_filling


@pytest.fixture(scope='function')
def prepared_burger(bun, sauce, filling):
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)
    return burger