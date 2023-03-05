import os

import pytest

from core.create_csv_file import CreateCsvFile


def test_it_should_create_a_csv_file():
    csv_file = CreateCsvFile('test_vendas', 15)
    csv_file.execute()

    assert os.path.isfile('test_vendas.csv') == True


if __name__ == '__main__':
    pytest.main()
