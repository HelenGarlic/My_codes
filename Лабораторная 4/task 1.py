import json

def task() -> float:
    with open('input.json', 'r') as file_1:
        json_data = json.load(file_1)
    #    total = 0
    #    for d in json_data:
    #        prod = 1                  '''Эти циклы в одной строке'''
    #        for i in d.values():
    #            prod *= i
    #        total += prod
        total = sum(item["score"]*item["weight"] for item in json_data)

        return(f"{total:.3f}")

print(task())

