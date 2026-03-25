import json

data={
    "Name":"Abc",
    "Age":30
}

json_str=json.dumps(data)
print(json_str)

# PS D:\PY\Modules> python -u "d:\PY\Modules\JSON\dumps.py"
# {"Name": "Abc", "Age": 30}
# python obj to -> json obj

json_str=json.dumps(data,indent=4)
print(json_str)

# {
#     "Name": "Abc",
#     "Age": 30
# }
# print json obj into pritty format

json_str=json.dumps(data,indent=4,sort_keys=True)
print(json_str)

# {
#     "Age": 30,
#     "Name": "Abc"
# }
# sort dict keys alphabetically 