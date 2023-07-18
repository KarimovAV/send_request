from src.configuration import *
from src.schemas.users import *
from src.base_class.checking_methods import CheckingMethods
from src.tests.utilities.conftest import set_up


def test_get_users_default(set_up):
    cm = CheckingMethods(BASE_URL)

    cm.check_status_code(cm.get(users_end_point), 200)
    cm.check_schema_body(cm.get(users_end_point), users_get_json_schema)
    cm.check_count_returned_records(cm.get(users_end_point))


def test_get_companies_no_default(set_up):
    cm = CheckingMethods(BASE_URL)

    cm.check_status_code(cm.get(users_end_point), 200)
    cm.check_schema_body(cm.get(users_end_point), users_get_json_schema)
    cm.check_count_returned_records(cm.get(f'{users_end_point}?limit=10'), limit=10)