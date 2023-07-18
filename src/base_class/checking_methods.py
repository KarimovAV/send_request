import json
from src.enums.global_enums import ErrorAssert
from src.base_class.http_methods import HttpsMethods
from jsonschema import validate


class CheckingMethods(HttpsMethods):
    """Methods For Checking Success Of Request"""
    def __init__(self, base_url):
        super().__init__(base_url)
        self.base_url = base_url

    """Checking Status Code"""
    @staticmethod
    def check_status_code(func_request, expected_status_code):
        print(f'{func_request.status_code} == {expected_status_code}')
        assert func_request.status_code == expected_status_code, ErrorAssert.WRONG_STATUS_CODE.value
        print('Checking status code successful')

    """Checking JSON-Schema Of Body Response"""
    @staticmethod
    def check_schema_body(func_request, schema_json):
        validate(func_request.json(), schema_json)
        print('Validate JSON-schema is success')

    """Checking Count Of Returned Records. Default = 3"""
    @staticmethod
    def check_count_returned_records(func_request, limit=3):
        count_data = json.loads(func_request.text)
        print(f'Returned records: {len(count_data["data"])} = {limit}')
        assert len(count_data['data']) == limit, ErrorAssert.WRONG_RETURNED_RECORDS.value

    """Checking Keys On Acceptable Values From Enums"""
    @staticmethod
    def check_values_from_enums(func_request, list_enums, key_check_one, key_check_two):
        json_from_request = json.loads(func_request.text)[key_check_one]
        for i_list in json_from_request:
            assert i_list[key_check_two] in list_enums, ErrorAssert.WRONG_POSSIBLE_ENUMS
            print(f'{i_list[key_check_two]} in {list_enums}')



