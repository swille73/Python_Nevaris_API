
base_url = "http://localhost:8500"

def get_value(dict, key):
    if key in dict:
        return dict[key]
    else:
        return None