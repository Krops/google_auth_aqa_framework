def get_request_param_value_by_name(params: tuple[dict], name: str) -> str:
    for param in params:
        if param.get(name):
            return param
    return ''
