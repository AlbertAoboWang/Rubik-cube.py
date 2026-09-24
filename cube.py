cube = {
    "U" : ["W"] * 9,
    "D" : ["Y"] * 9,
    "F" : ["G"] * 9,
    "B" : ["B"] * 9,
    "L" : ["O"] * 9,
    "R" : ["R"] * 9
}
for face in cube:
    print(face,cube[face])