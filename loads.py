import json

json_data='{"Name":"Johan","Age":20}'
py_data=json.loads(json_data)
print(py_data)
print(py_data["Name"])

# {'Name': 'Johan', 'Age': 20}
# Johan
# Convert json data into py data 