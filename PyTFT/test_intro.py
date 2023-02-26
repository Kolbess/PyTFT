
from unittest import mock
from intro import intro


get_input_usage = 0


def mock_time_sleep(sleeptime):
    pass


def mock_get_input(text):
    print(text)
    global get_input_usage
    get_input_usage += 1
    if get_input_usage == 4:
        return 'start'
    else:
        return str(get_input_usage)


def test_intro():
    with mock.patch('intro.get_input', side_effect=mock_get_input):
        with mock.patch('time.sleep', side_effect=mock_time_sleep):
            intro()

