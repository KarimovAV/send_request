import enum


class ErrorAssert(enum.Enum):
    WRONG_STATUS_CODE = 'Status Code Does Not Match The Expected'
    WRONG_JSON_SCHEMA = 'JSON-Schema Does Not Match The Expected'
    WRONG_RETURNED_RECORDS = 'Count Of Returned Records Does Not Match The Expected'
    WRONG_POSSIBLE_ENUMS = 'Values For Key Does Match Possible From Enums'
