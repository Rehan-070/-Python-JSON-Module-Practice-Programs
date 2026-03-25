import json

try:
    with open("data.json",'r',encoding='utf-8') as file:
        data=json.load(file)
    print("data : ",data)
    print("Accessing Data : ",data["name"])
    print("data Type : ",type(data))
except FileNotFoundError:
    print("File is missing")
except json.JSONDecodeError as e:
    print(f"Somthing error {e}")



# data :  {'name': 'hi', 'age': 10}
# Accessing Data :  hi
# data Type :  <class 'dict'>
# loads the content of data.json file 