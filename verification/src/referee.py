from checkio_referee import RefereeBase
from checkio_referee.covercode import py_tuple

import settings
import settings_env
from tests import TESTS


class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "total_cost"
    ENV_COVERCODE = {
        "python_2": py_tuple,
        "python_3": py_tuple,
        "javascript": None
    }
