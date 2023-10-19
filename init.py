import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# 读取.json文件
file_path = 'conf.json'
json_data = read_json_file(file_path)
# 提取信息
key = json_data["key"]


