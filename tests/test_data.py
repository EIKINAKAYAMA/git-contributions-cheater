from data.dataByAnswer import get_data_per_month


def test_data_generation_case1():
    target_year = 2023
    target_month = 1
    entered_day = 1
    is_freq_random = 'Y'
    entered_freq = 1

    expected_output = [
        ["2023-01-01", 1],
    ]

    output_data = get_data_per_month(target_year, target_month, entered_day,
                                     is_freq_random, entered_freq)
    assert output_data == expected_output


def test_data_generation_case2():
    target_year = 2022
    target_month = 2
    entered_day = 32  # weekends
    is_freq_random = 'N'
    entered_freq = 10

    expected_output = [
        ["2022-02-05", 10],
        ["2022-02-06", 10],
        ["2022-02-12", 10],
        ["2022-02-13", 10],
        ["2022-02-19", 10],
        ["2022-02-20", 10],
        ["2022-02-26", 10],
        ["2022-02-27", 10]
    ]

    output_data = get_data_per_month(target_year, target_month, entered_day,
                                     is_freq_random, entered_freq)
    assert output_data == expected_output


def test_data_generation_case3():
    target_year = 2023
    target_month = 12
    entered_day = 0   # weekdays
    is_freq_random = 'N'
    entered_freq = 10

    expected_output = [
        ["2023-12-01", 10],
        ["2023-12-04", 10],
        ["2023-12-05", 10],
        ["2023-12-06", 10],
        ["2023-12-07", 10],
        ["2023-12-08", 10],
        ["2023-12-11", 10],
        ["2023-12-12", 10],
        ["2023-12-13", 10],
        ["2023-12-14", 10],
        ["2023-12-15", 10],
        ["2023-12-18", 10],
        ["2023-12-19", 10],
        ["2023-12-20", 10],
        ["2023-12-21", 10],
        ["2023-12-22", 10],
        ["2023-12-25", 10],
        ["2023-12-26", 10],
        ["2023-12-27", 10],
        ["2023-12-28", 10],
        ["2023-12-29", 10]
    ]

    output_data = get_data_per_month(target_year, target_month, entered_day,
                                     is_freq_random, entered_freq)
    assert output_data == expected_output


def test_data_generation_case4():
    target_year = 2023
    entered_day = 31
    is_freq_random = 'N'
    entered_freq = 10
    output_data = []

    expected_output = [
        ["2023-01-31", 10],
        ["2023-02-31", 10],
        ["2023-03-31", 10],
        ["2023-04-31", 10],
        ["2023-05-31", 10],
        ["2023-06-31", 10],
        ["2023-07-31", 10],
        ["2023-08-31", 10],
        ["2023-09-31", 10],
        ["2023-10-31", 10],
        ["2023-11-31", 10],
        ["2023-12-31", 10]
    ]
    for month in range(1, 13):
        data = get_data_per_month(target_year, month, entered_day,
                                  is_freq_random, entered_freq)
        output_data.extend(data)

    assert output_data == expected_output


def test_data_generation_case5():
    target_year = 2099
    target_month = 2
    entered_day = 99  # all days
    is_freq_random = 'N'
    entered_freq = 10

    expected_output = [
        ["2099-02-01", 10],
        ["2099-02-02", 10],
        ["2099-02-03", 10],
        ["2099-02-04", 10],
        ["2099-02-05", 10],
        ["2099-02-06", 10],
        ["2099-02-07", 10],
        ["2099-02-08", 10],
        ["2099-02-09", 10],
        ["2099-02-10", 10],
        ["2099-02-11", 10],
        ["2099-02-12", 10],
        ["2099-02-13", 10],
        ["2099-02-14", 10],
        ["2099-02-15", 10],
        ["2099-02-16", 10],
        ["2099-02-17", 10],
        ["2099-02-18", 10],
        ["2099-02-19", 10],
        ["2099-02-20", 10],
        ["2099-02-21", 10],
        ["2099-02-22", 10],
        ["2099-02-23", 10],
        ["2099-02-24", 10],
        ["2099-02-25", 10],
        ["2099-02-26", 10],
        ["2099-02-27", 10],
        ["2099-02-28", 10]
    ]

    output_data = get_data_per_month(target_year, target_month, entered_day,
                                     is_freq_random, entered_freq)
    assert output_data == expected_output
