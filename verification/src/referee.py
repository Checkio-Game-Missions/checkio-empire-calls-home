from checkio_referee import RefereeBase
from checkio_referee import covercodes, representations

import settings
import settings_env
from tests import TESTS


class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "total_cost"
    CALLED_REPRESENTATIONS = {
        "python_3": representations.py_tuple_representation,
        "python_2": representations.py_tuple_representation,
    }
    ENV_COVERCODE = {
        "python_2": covercodes.py_tuple,
        "python_3": covercodes.py_tuple,
        "javascript": None
    }
