import argparse
import json
import random
import re


__COUNTER__ = 20


def open_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    f.close()
    return data




def generate(n=10):
    pattern_possibilities = open_json("train\\patterns_possibilities.json")["possibilities"]
    segment_possibilities = open_json("train\\res_possibilities.json")
    passwords = {}
    for i in range(n):
        pattern_choice = random.choices(list(pattern_possibilities.keys()), weights=list(pattern_possibilities.values()), k=1)[0]
        #将pattern_choice中LDS进行拆分
        pattern_choice_split = re.findall(r'[LDS][0-9]+', pattern_choice)
        #print(pattern_choice_split)
        password = ""
        for segment in pattern_choice_split:
            if (segment not in segment_possibilities):
                continue
            segment_choice = random.choices(list(segment_possibilities[segment].keys()), weights=list(segment_possibilities[segment].values()), k=1)[0]
            password += segment_choice
        #print(password)
        passwords[i] = password
    
    with open("train\\generated_passwords.json", "w") as f:
        json.dump(passwords, f, indent=4, separators=(',', ': '))
    f.close()
    





if __name__ == "__main__":
    generate(__COUNTER__)