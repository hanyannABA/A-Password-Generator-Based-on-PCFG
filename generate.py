import json



__Pattern__="train\\patterns_possibilities.json"
__Segment__="train\\res_possibilities.json"


def open_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    f.close()
    return data

def prase_structure(password):
    pattern = []
    i=0
    j=0
    while i < len(password):
        if password[i].isalpha():
            j+=1
        i+=1
    pattern.append(f"L{j}")
    i=0
    j=0
    while i < len(password):
        if password[i].isdigit():
            j+=1
        i+=1
    pattern.append(f"D{j}")
    i=0
    j=0
    while i < len(password):
        if not password[i].isalpha() and not password[i].isdigit():
            j+=1
        i+=1
    pattern.append(f"S{j}")
    
    
    return ''.join(pattern)


def extract_password_segments(password):
    segment = []
    i = 0
    while i < len(password):
        if password[i].isalpha():
            j = i
            while j < len(password) and password[j].isalpha():
                j += 1
            segment.append(("L%d" % (j - i), password[i:j]))
            i = j
        elif password[i].isdigit():
            j = i
            while j < len(password) and password[j].isdigit():
                j += 1
            segment.append(("D%d" % (j - i), password[i:j]))
            i = j
        else:
            j = i
            while j < len(password) and not password[j].isalpha() and not password[j].isdigit():
                j += 1
            segment.append(("S%d" % (j - i), password[i:j]))
            i = j
    return segment


def generate():
    pattern_possibilities = open_json(__Pattern__)
    segment_possibilities = open_json(__Segment__)
    #print("pattern possibilities:", pattern_possibilities)
    #print("segment possibilities:", segment_possibilities)
    with open("train\\password_given.txt", "r") as f:

        passwords = f.read().splitlines()
    f.close()
    #print("password:", passwords)

    password_patterns = [prase_structure(pw) for pw in passwords]
    #print("password patterns:", password_patterns)
    password_segment = [extract_password_segments(pw) for pw in passwords]
    #print("password segments:", password_segment)

    password_possibilities = dict.fromkeys(passwords, 0)
    length=len(passwords)
    for i in range(length):
        password=passwords[i]
        pattern=password_patterns[i]
        segment=password_segment[i]
        #print("password:", password)
        #print("pattern:", pattern)
        #print("segment:", segment)
        password_possibilities[password]=pattern_possibilities["possibilities"][pattern]
        for seg in segment:
            password_possibilities[password]*=segment_possibilities[seg[0]][seg[1]]

        
    print("password possibilities:", password_possibilities)


    with open("train\\generate_password_prob.json", "w") as f:
        json.dump({"password_possibilities": password_possibilities}, f, indent=4, separators=(',', ': '))
    f.close()
        





if __name__ == "__main__":
    generate()