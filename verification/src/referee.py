from checkio_referee import RefereeBase
from checkio_referee import covercodes, representations


import settings_env
from tests import TESTS


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "total_cost"
    CALLED_REPRESENTATIONS = {
        "python_3": representations.py_tuple_representation,
        "python_2": representations.py_tuple_representation,
    }
    ENV_COVERCODE = {
        "python_2": covercodes.py_tuple,
        "python_3": covercodes.py_tuple,
        "javascript": None
    }
