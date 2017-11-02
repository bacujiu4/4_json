#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import argparse

def load_data(file_path):
    with open(file_path, 'r') as handler:
        raw_json_data = handler.read()
        parsed_json_data = json.loads(raw_json_data)
    return parsed_json_data

    #with open(file_path, 'r') as file_obj:
    #    return json.loads(file_obj)

def pretty_print_json(parsed_json_data):
    pretty_json_data = json.dumps(parsed_json_data, indent=4, ensure_ascii = False)
    return pretty_json_data
    #return json.dumps(json.loads(), indent=2, ensure_ascii = False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path')
    args = parser.parse_args()
    print(pretty_print_json((load_data(args.file_path))))
