cube = {
    "U" : ["W"] * 9,
    "D" : ["Y"] * 9,
    "F" : ["G"] * 9,
    "B" : ["B"] * 9,
    "L" : ["O"] * 9,
    "R" : ["R"] * 9
}
for k,v in cube.items():
    print(k)
    print(v)

clockwise_rotated = [
    6,3,0,
    7,4,1,
    8,5,2
] 
