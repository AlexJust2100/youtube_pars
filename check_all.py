import itertools
import requests
import json
import time

def get_substring_around_pair(input_value, pair):
    index = input_value.find(pair)
    if index == -1:
        return {"before": input_value, "after": ""}
    before = input_value[:index]
    after = input_value[index + len(pair):]
    return {"before": before, "after": after}

def ptable_check(input_value):
    table = {
        "H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10,
        "Na": 11, "Mg": 12, "Al": 13, "Si": 14, "P": 15, "S": 16, "Cl": 17, "Ar": 18, "K": 19, "Ca": 20,
        "Sc": 21, "Ti": 22, "V": 23, "Cr": 24, "Mn": 25, "Fe": 26, "Co": 27, "Ni": 28, "Cu": 29, "Zn": 30,
        "Ga": 31, "Ge": 32, "As": 33, "Se": 34, "Br": 35, "Kr": 36, "Rb": 37, "Sr": 38, "Y": 39, "Zr": 40,
        "Nb": 41, "Mo": 42, "Tc": 43, "Ru": 44, "Rh": 45, "Pd": 46, "Ag": 47, "Cd": 48, "In": 49, "Sn": 50,
        "Sb": 51, "Te": 52, "I": 53, "Xe": 54, "Cs": 55, "Ba": 56, "La": 57, "Ce": 58, "Pr": 59, "Nd": 60,
        "Pm": 61, "Sm": 62, "Eu": 63, "Gd": 64, "Tb": 65, "Dy": 66, "Ho": 67, "Er": 68, "Tm": 69, "Yb": 70,
        "Lu": 71, "Hf": 72, "Ta": 73, "W": 74, "Re": 75, "Os": 76, "Ir": 77, "Pt": 78, "Au": 79, "Hg": 80,
        "Tl": 81, "Pb": 82, "Bi": 83, "Po": 84, "At": 85, "Rn": 86, "Fr": 87, "Ra": 88, "Ac": 89, "Th": 90,
        "Pa": 91, "U": 92, "Np": 93, "Pu": 94, "Am": 95, "Cm": 96, "Bk": 97, "Cf": 98, "Es": 99, "Fm": 100,
        "Md": 101, "No": 102, "Lr": 103, "Rf": 104, "Db": 105, "Sg": 106, "Bh": 107, "Hs": 108, "Mt": 109, "Ds": 110,
        "Rg": 111, "Cn": 112, "Nh": 113, "Fl": 114, "Mc": 115, "Lv": 116, "Ts": 117, "Og": 118
    }

    sum_value = 0
    i = 0

    while i < len(input_value):
        current_char = input_value[i]
        two_characters = ""

        try:
            two_characters = input_value[i:i + 2]
        except:
            pass

        if two_characters != "" and two_characters in table:
            sum_value += table[two_characters]
            substrings = get_substring_around_pair(input_value, two_characters)
            input_value = substrings["before"] + "__" + substrings["after"]
        else:
            if current_char in table:
                sum_value += table[current_char]

        i += 1

    return sum_value < 200
    

headers = {
    'Server': 'cloudfare',
    'Vary': 'Accept-Encoding',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}
characters = "0123456789abcdefghijklmnopqrstuvwxyzABEFGHIJKNOPQRSTUVWXYZ-_"

last_try_url = "https://getpantry.cloud/apiv1/pantry/3460f78b-e943-4035-b59a-54e966f8a374/basket/last_try"
response = requests.get(last_try_url, headers=headers)
body_last_try = response.json()
last_try = body_last_try["url"]
index = 1

for i, char in enumerate(last_try):
    position = characters.index(char)
    weight = 60 ** (11 - i - 1)
    index += position * weight
maybe = []
combinations = itertools.islice(itertools.product(characters, repeat=11), index, index + 10000)
for combo in combinations:
    string = ''.join(combo)
    if 17 >= sum(int(char) for char in string if char.isdigit()) and ptable_check(string):
        maybe.append(string)
        if len(maybe) == 200:
            data = {'urls':maybe}
            response = requests.put("https://getpantry.cloud/apiv1/pantry/3460f78b-e943-4035-b59a-54e966f8a374/basket/MAYBE", headers=headers, json=data)
            time.sleep(1)
            maybe = []
    last_try = string
data = {'urls':maybe}
response = requests.put("https://getpantry.cloud/apiv1/pantry/3460f78b-e943-4035-b59a-54e966f8a374/basket/MAYBE", headers=headers, json=data)  
data = {"url": last_try}
time.sleep(2)
request = requests.post("https://getpantry.cloud/apiv1/pantry/3460f78b-e943-4035-b59a-54e966f8a374/basket/last_try", headers=headers, json=data)            
