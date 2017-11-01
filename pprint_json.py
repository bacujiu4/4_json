#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import argparse

def load_data(filepath):
     data = open(filepath, 'r').read()
     print(pretty_print_json(data))

def pretty_print_json(data):
     return json.dumps(json.loads(data), indent=2, ensure_ascii = False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    args = parser.parse_args()
    load_data(args.filepath)
