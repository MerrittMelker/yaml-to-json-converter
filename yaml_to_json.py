import os
import json
import yaml


def convert_yaml_to_json(yaml_path, json_path):
    with open(yaml_path, 'r', encoding='utf-8') as yf:
        data = yaml.safe_load(yf)
    with open(json_path, 'w', encoding='utf-8') as jf:
        json.dump(data, jf, indent=2)


def main(directory):
    for root, _, files in os.walk(directory):
        for fname in files:
            if fname.lower().endswith(('.yaml', '.yml')):
                yaml_file = os.path.join(root, fname)
                json_file = os.path.splitext(yaml_file)[0] + '.json'
                try:
                    convert_yaml_to_json(yaml_file, json_file)
                    print(f"Converted {yaml_file} -> {json_file}")
                except Exception as e:
                    print(f"Failed {yaml_file}: {e}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: python yaml_to_json.py <directory>")
        exit(1)
    main(sys.argv[1])
