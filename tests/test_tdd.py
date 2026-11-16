from src.user_data_pipeline.calculate_tdd import calculate_total


def test_calculate_total():
    expenses = [10, 20, 30]

    result = calculate_total(expenses)

    assert result == 60


def test_calculate_total_():
    pass


# powiedziec chatowi zeby rozbijal problem uzywajac elephant carpaccio
