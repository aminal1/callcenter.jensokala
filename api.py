import json 


with open ("response_1686250644208.json",'r', errors='ignore', encoding='UTF-8') as json_data:
    data = json.load(json_data)
    a=0
    for item in data :
        if a < 10 :
            print (item)
            a+=1
        else:
            break

