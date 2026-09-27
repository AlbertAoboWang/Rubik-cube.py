import copy
face_names = ["U","D","F","B","L","R"]
original_cube = []
cube = [
    [[],
     [],
     []],
    [[],
     [],
     []],
    [[],
     [],
     []],
    [[],
     [],
     []],
    [[],
     [],
     []],
    [[],
     [],
     []]
]
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
def rotate_clockwise2D(face):
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
def rotate_counterclockwise2D(face1):
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

for q in range(6):
    print(face_names[q])
    for a in range(3):
        scrambled_face = input()
        for z in scrambled_face:
            if len(scrambled_face) == 3:
                cube[q][a].append(z)
                continue
            else:
                print("invaild input")
                input_vaild = False
                exit()
        
def move_U_clockwise(old_cube):

    new_face = rotate_clockwise2D(old_cube[0])
    old_cube[0] = new_face
    old_faces = [
    old_cube[2][0],#front
    old_cube[3][0],#back
    old_cube[4][0],#left
    old_cube[5][0]#right
]
    old_cube[2][0] = old_faces[3]
    old_cube[3][0] = old_faces[2]
    old_cube[4][0] = old_faces[0]
    old_cube[5][0] = old_faces[1]
    return old_cube

def move_U_counterclockwise(old_cube):

    new_face = rotate_counterclockwise2D(old_cube[0])
    old_cube[0] = new_face
    old_faces = [
    old_cube[2][0],#front
    old_cube[3][0],#back
    old_cube[4][0],#left
    old_cube[5][0]#right
]
    old_cube[2][0] = old_faces[2]
    old_cube[3][0] = old_faces[3]
    old_cube[4][0] = old_faces[1]
    old_cube[5][0] = old_faces[0]
    return old_cube

original_cube = copy.deepcopy(cube)
move_U_clockwise(cube)
move_U_counterclockwise(cube)
if cube == original_cube:
    print("YES")
else:
    print("NO")