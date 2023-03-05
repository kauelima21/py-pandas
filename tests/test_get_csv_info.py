import pytest

from core.get_csv_info import GetCSVInfo


def test_it_should_return_total_sales():
    csv_info = GetCSVInfo('test_vendas.csv')
    total_sales = csv_info.get_total_sales()

    assert total_sales == 3797545.96


if __name__ == '__main__':
    pytest.main()
