from src.user_data_pipeline.calculate_tdd import calculate_total


def test_calculate_total():
    expenses = [10, 20, 30]

    result = calculate_total(expenses)

    assert result == 60


# @pytest.mark.superfast # oznaczanie wolnych testow
# def test_calculate_total_(valid_user_data):
#     print(valid_user_data.get("id"))
#     assert False


# powiedziec chatowi zeby rozbijal problem uzywajac elephant carpaccio
