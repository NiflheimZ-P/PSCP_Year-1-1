"""Ejudge"""
import json
def main():
    """Impostor"""
    person, dead, alive, impos = {}, {}, {}, 0
    while True:
        tmp = input()
        if tmp.upper() == "END":
            break
        if tmp.upper() == "START":
            continue
        if tmp[0] == "{":
            person.update(json.loads(tmp))
        else:
            dead.update({tmp: person[tmp]})
    for i in person:
        if i not in dead:
            alive.update({i:person[i]})
    for i in alive:
        if person[i] == "Impostor":
            impos += 1
    print("%d Impostor Remains" %impos)
    print("***Alive***")
    for i in sorted(alive.items(), key=lambda item: item[0]):
        print(*i, sep=" : ")
    print("***Dead***")
    for i in sorted(dead.items(), key=lambda item: item[0]):
        print(*i, sep=" : ")
main()
