import json

def open_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    f.close()
    return data





if __name__ == "__main__":
    patterns_possibilities = open_json("train\\patterns_possibilities.json")["possibilities"]
    segment_possibilities = open_json("train\\res_possibilities.json")
    #print(patterns_possibilities)
    patterns_possibilities = sorted(patterns_possibilities.items(), key=lambda x: x[1], reverse=True)
    L4_segment_possibilities = sorted(segment_possibilities["L4"].items(), key=lambda x: x[1], reverse=True)
    D3_segment_possibilities = sorted(segment_possibilities["D3"].items(), key=lambda x: x[1], reverse=True)
    S2_segment_possibilities = sorted(segment_possibilities["S2"].items(), key=lambda x: x[1], reverse=True)
    with open("train\\possibilities_top5.json", "w") as f:
        json.dump({"patterns_possibilities": patterns_possibilities[:5], "L4_segment_possibilities": L4_segment_possibilities[:5], "D3_segment_possibilities": D3_segment_possibilities[:5], "S2_segment_possibilities": S2_segment_possibilities[:5]}, f, indent=4, separators=(',', ': '))
    f.close()
    