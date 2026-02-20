import textwrap


def split(dashes):
    if len(dashes) == 1:
        return dashes
    splitted = textwrap.wrap(dashes, len(dashes) // 3)
    splitted[0] = split(splitted[0])
    splitted[1] = splitted[1].replace("-", " ")
    splitted[2] = split(splitted[2])
    return splitted[0] + splitted[1] + splitted[2]


while True:
    try:
        num = int(input())
        print(split("-" * (3**num)))
    except:
        break
