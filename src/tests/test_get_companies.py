from src.data.companies_status import companies_status
from src.configuration import *
from src.schemas.companies import *
from src.base_class.checking_methods import CheckingMethods
from src.tests.utilities.conftest import set_up


def test_get_default_limit(set_up):
    cm = CheckingMethods(BASE_URL)

    cm.check_status_code(cm.get(companies_get_endpoint), 200)
    cm.check_schema_body(cm.get(companies_get_endpoint), companies_get_json_schema)
    cm.check_count_returned_records(cm.get(companies_get_endpoint))
    cm.check_values_from_enums(cm.get(companies_get_endpoint), companies_status, 'data', 'company_status')


def test_get_no_default_limit(set_up):
    cm = CheckingMethods(BASE_URL)

    cm.check_status_code(cm.get(companies_get_endpoint), 200)
    cm.check_schema_body(cm.get(companies_get_endpoint), companies_get_json_schema)
    cm.check_count_returned_records(cm.get(f'{companies_get_endpoint}?limit=7'), limit=7)
    cm.check_values_from_enums(cm.get(companies_get_endpoint), companies_status, 'data', 'company_status')