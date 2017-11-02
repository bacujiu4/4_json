import json
import argparse


def load_data(file_path):
    with open(file_path, 'r') as opened_file:
        raw_json_data = opened_file.read()
        parsed_json_data = json.loads(raw_json_data)
    return parsed_json_data


def prettify_json_data(parsed_json_data):
    pretty_json_data = json.dumps(
        parsed_json_data, indent=4, ensure_ascii=False)
    return pretty_json_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path')
    args = parser.parse_args()
    print(prettify_json_data(load_data(args.file_path)))
