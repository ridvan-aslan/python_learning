import json

person_string = '{"name": "Rıdvan", "languages": ["Python", "C#"]}'

result = json.loads(person_string)

# print(type(result))
# print(result["name"])
# print(result["languages"])

# with open("advanced-modules/person.json", encoding="utf-8") as f:
#     data = json.load(f)
#     print(data)
#     print(data["name"])
#     print(data["languages"])

person_dict = {"name": "Rıdvan", "languages": ["Python", "C#"]}

# result = json.dumps(person_dict)

# print(result)
# print(type(result))

with open("advanced-modules/person.json", "w", encoding="utf-8") as f:
    json.dump(person_dict, f, ensure_ascii=False, indent=4, sort_keys= True)

person_dict = json.loads(person_string)

result = json.dumps(person_dict, indent=4, sort_keys=True, ensure_ascii=False)

print(result)