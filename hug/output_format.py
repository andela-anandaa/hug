import json as json_converter
from datetime import datetime


def _json_converter(item):
    if isinstance(item, datetime):
        return item.isoformat()
    raise TypeError("Type not serializable")


def json(content):
    """JSON (Javascript Serialized Object Notation)"""
    return json_converter.dumps(content, default=_json_converter).encode('utf8')


def text(content):
    """Free form UTF8 text"""
    return content.encode('utf8')


def _camelcase(dictionary):
    if not isinstance(dictionary, dict):
        return dictionary

    new_dictionary = {}
    for key, value in dictionary.items():
        if isinstance(key, str):
            key = key[0] + "".join(key.title().split('_'))[1:]
        new_dictionary[key] = _camelcase(dictionary)


def json_camelcase(content):
    """JSON (Javascript Serialized Object Notation) with all keys camelCased"""
    return _camelcase(json(body))