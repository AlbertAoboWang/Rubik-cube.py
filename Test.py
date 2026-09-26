face_names = ["U","D","F","B","L","R"]
cube = []
input_vaild = True
fixed_cube = {
    "U" : ["W"],
    "D" : ["Y"],
    "F" : ["G"],
    "B" : ["B"],
    "L" : ["O"],
    "R" : ["R"]
}
clockwise_rotated = [
    [6,3,0],
    [7,4,1],
    [8,5,2]
]  
counterclockwise_rotated = [
    [2,5,8],
    [1,4,7],
    [0,3,6]
]
regular_rotated = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]

for i in range(6):
    print(face_names[i])
    for j in range(3):
        scrambled_face = input()
        for i in scrambled_face:
            if len(scrambled_face) == 3:
                cube.append(i)
                continue
            else:
                print("invaild input")
                input_vaild = False
    break
