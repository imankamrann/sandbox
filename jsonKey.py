import json,silly

def getPerson():
    person = dict(name=silly.name(),age=silly.number())
    return person

#Reading
with open("data.json", "r") as f:
        json_content = json.loads(f.read())
print(json_content)

#Writing
person = {'name': 'Charles', 'age': 33}
with open("person.json", "w") as f:
    f.write(json.dumps(person))

#Writing a person using silly module
with open("10Person.json", "w") as f:
    for _ in range(10):
        f.write(json.dumps(getPerson()))







