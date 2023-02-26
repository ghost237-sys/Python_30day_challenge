#JSON files
#JavaScript Object Notation is a popular way to format data as a single huma-readable string.
#Python's json Module handles all the details of translating between a string with JSON data and Python values and Pyhthon values for the json.loads() and json.dumps() functions.

#Reading JSON with the loads() Function
import json
StringofJsonData = '{"name":"Zophie","isCat":true,"miceCaught":0,"felineIO":null}'#note JSON strings always use double quotes
jsondataAsPythonValue = json.loads(StringofJsonData)
print(jsondataAsPythonValue)
#displays....{'name': 'Zophie', 'isCat': True, 'miceCaught': 0, 'felineIO': None}
#the data is returned as a Python dictionary


#writing JSON with the dumps()Function
#json.dumps() will translate a python value into a string of JSON-formatted data
pythonValue = {'isCat': True,'miceCaught':0,'name':'Zophie'}
print(json.dumps(pythonValue))
#displays {"isCat": true, "miceCaught": 0, "name": "Zophie"}
