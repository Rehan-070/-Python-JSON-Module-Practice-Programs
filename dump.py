import json

data={"name":"hi","age":10}

with open("data.json",'w') as fp:
    json.dump(data,fp)


# If file dosent exist it will create file with name data.json and write data into it.