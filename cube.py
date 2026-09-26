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
def rotate_clockwise(face):
    clockwise_rotated = [
        [face[2][0],face[1][0],face[0][0]],
        [face[2][1],face[1][1],face[0][1]],
        [face[2][2],face[1][2],face[0][2]]
    ]
    return clockwise_rotated
counterclockwise_rotated = [
    [2,5,8],
    [1,4,7],
    [0,3,6]
]
def rotate_counterclockwise(face1):
    counterclockwise_rotated = [
        [face1[0][2],face1[1][2],face1[2][2]],
        [face1[0][1],face1[1][1],face1[2][1]],
        [face1[0][0],face1[1][0],face1[2][0]]
    ]
    return counterclockwise_rotated
regular_rotated = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]

for q in range(1):
    print(face_names[q])
    for a in range(3):
        scrambled_face = input()
        for z in scrambled_face:
            if len(scrambled_face) == 3:
                cube.append(z)
                continue
            else:
                print("invaild input")
                input_vaild = False
    break
cube_face = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]
def rotate_clockwise(face):
    clockwise_rotated = [
        [face[2][0],face[1][0],face[0][0]],
        [face[2][1],face[1][1],face[0][1]],
        [face[2][2],face[1][2],face[0][2]]
    ]
    return clockwise_rotated


print(rotate_counterclockwise(cube_face))
print(rotate_clockwise(cube_face))
print(cube)