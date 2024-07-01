import json


def seach_different(arg1, arg2):
    first = json.load(open(f'gendiff/{arg1}'))
    second = json.load(open(f'gendiff/{arg2}'))
    list_of_all = sorted(set(first) | set(second))
    print("{")
    for i in list_of_all:
        if first.get(i) == None:
            sign = "+ "
        elif second.get(i) == None:
            sign = "- "
        else:
            sign = "  "
        print(f"  {sign}{i}: {first.get(i, second.get(i))}")
    return
            
    
