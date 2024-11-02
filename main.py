a = {
    "LOL":"Laughing Out Loud",
    "LMAO":"Laughing My A$$ Out",
    "ROFL":"Rolling On the Floor Laughing",
    "CRINGE":"Gave second hand embarassment",
    "MEWING":"Mouth exercise to enhance the jawline",
    "RIZZ":"Slang for charisma",
    "ALFA":"Leader",
    "ALPHA":"Leader",
    "AITA":"Am I The A$$"
}
print(a.keys())
while True: 
    req = input("Input word").upper()
    if req in a.keys():
        print("Meaning:",a[req])
    elif req not in a.keys():
        print('not in diccionary')
    print("________________________________________________________________")
