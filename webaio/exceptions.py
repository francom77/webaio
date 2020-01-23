class APIException(Exception):
    status_code = 500
    detail = 'Default error message'
