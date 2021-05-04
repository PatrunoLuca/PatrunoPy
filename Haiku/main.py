from json import load
from random import choice

def extract(filename):
    with open("%s.json" % filename, "r") as outfile:
        return load(outfile)

def generate(json):
    return "\n".join(
        [
            str(choice(json["verso %s" % str(i)]))
            for i in range(1, len(json.items()) + 1)
            ]
        )

if __name__ == "__main__":
    json = extract("haiku")
    haiku = generate(json)
    print(haiku)