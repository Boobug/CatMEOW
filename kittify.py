from responseLink import get_response
import re

def get_gender_from_response(nama):
    legends_url = f"https://maplelegends.com/api/getavatar?name={nama}&mount=1&animated=1&face=f2"
    response_url = get_response(legends_url)
    result = re.findall(r":(\w+),", response_url)

    males = []
    females = []
    inconsequential = []

    for item in result[2:-4]:
        if item[-4] == '0':
            males.append(item)
        elif item[-4] == '1':
            females.append(item)
        else:
            inconsequential.append(item)

    if len(males) > 0 and len(females) == 0:
        return 0 # Male only
    elif len(females) > 0 and len(males) == 0:
        return 1 # Female only
    else:
        return -1 # Both male and female, or everything is inconsequential

    # If gender is inconclusive, return -1 and request input from the user
    return -1 

nama = 'pops'
print(get_gender_from_response(nama))