import sys
import argparse
import os
import tempfile
import json
#print(sys.argv)
parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")

namespace = parser.parse_args()
#print(namespace)
#print(type(namespace))

dict_var = vars(namespace)
#dict_var = {"key":'aa', "val":2}
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if dict_var.get("val") == None:
    #Get value
    if os.path.exists(storage_path):
        with open(storage_path, "r") as f:
            file_data = f.read()
            if file_data == "":
                values_dict = {}
            else:
                values_dict = json.loads(file_data)
    else:
        values_dict = {}
    print(values_dict.get(dict_var.get('key', None)))
else:
    #Write value
    if os.path.exists(storage_path):
        with open(storage_path, "r") as f:
            file_data = f.read()
            if file_data == "":
                values_dict = {}
            else:
                values_dict = json.loads(file_data)
    else:
        values_dict = {}
    previous_value = values_dict.get(namespace.key)
    if previous_value == None:
        val = namespace.val
    else:
        val = f'{previous_value}, {namespace.val}'
    values_dict.update({namespace.key: val})
    with open(storage_path, 'w') as f:
        f.write(json.dumps(values_dict))
