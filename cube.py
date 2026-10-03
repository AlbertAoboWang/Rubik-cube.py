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

def rotate_clockwise2D(face):
    clockwise_rotated = [
        [face[2][0],face[1][0],face[0][0]],
        [face[2][1],face[1][1],face[0][1]],
        [face[2][2],face[1][2],face[0][2]]
    ]
    return clockwise_rotated

def rotate_counterclockwise2D(face1):
    counterclockwise_rotated = [
        [face1[0][2],face1[1][2],face1[2][2]],
        [face1[0][1],face1[1][1],face1[2][1]],
        [face1[0][0],face1[1][0],face1[2][0]]
    ]
    return counterclockwise_rotated

for q in range(6):
    print(face_names[q])
    for a in range(3):
        scrambled_face = input()
        for z in scrambled_face:
            if len(scrambled_face) == 3 and z in "WYGBOR":
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

def move_D_clockwise(old_cube):
    new_face = rotate_clockwise2D(old_cube[1])
    old_cube[1] = new_face
    old_faces = [
    old_cube[2][2],
    old_cube[3][2],
    old_cube[4][2],
    old_cube[5][2]
]
    old_cube[2][2] = old_faces[2]
    old_cube[3][2] = old_faces[3]
    old_cube[4][2] = old_faces[1]
    old_cube[5][2] = old_faces[0]
    return old_cube

def move_D_counterclockwise(old_cube):
    new_face = rotate_counterclockwise2D(old_cube[1])
    old_cube[1] = new_face
    old_faces = [
    old_cube[2][2],
    old_cube[3][2],
    old_cube[4][2],
    old_cube[5][2]
]
    old_cube[2][2] = old_faces[3]
    old_cube[3][2] = old_faces[2]
    old_cube[4][2] = old_faces[0]
    old_cube[5][2] = old_faces[1]
    return old_cube

def move_F_clockwise(old_cube):
    old_faces = [
        old_cube[5][0][0], old_cube[5][1][0], old_cube[5][2][0], 
        old_cube[4][0][2], old_cube[4][1][2], old_cube[4][2][2],  
        old_cube[1][0][0], old_cube[1][0][1], old_cube[1][0][2],  
        old_cube[0][2][0], old_cube[0][2][1], old_cube[0][2][2]   
    ]

    old_cube[2] = rotate_clockwise2D(old_cube[2])

    old_cube[5][0][0] = old_faces[6]
    old_cube[5][1][0] = old_faces[7]
    old_cube[5][2][0] = old_faces[8]

    old_cube[1][0][0] = old_faces[2]
    old_cube[1][0][1] = old_faces[1]
    old_cube[1][0][2] = old_faces[0]

    old_cube[4][0][2] = old_faces[11]
    old_cube[4][1][2] = old_faces[10]
    old_cube[4][2][2] = old_faces[9]

    old_cube[0][2][0] = old_faces[5]
    old_cube[0][2][1] = old_faces[4]
    old_cube[0][2][2] = old_faces[3]

    return old_cube

def move_F_counterclockwise(old_cube):
    old_faces = [
        old_cube[5][0][0], old_cube[5][1][0], old_cube[5][2][0],  
        old_cube[4][0][2], old_cube[4][1][2], old_cube[4][2][2],  
        old_cube[1][0][0], old_cube[1][0][1], old_cube[1][0][2], 
        old_cube[0][2][0], old_cube[0][2][1], old_cube[0][2][2]  
    ]

    old_cube[2] = rotate_counterclockwise2D(old_cube[2])

    old_cube[0][2][0] = old_faces[0]
    old_cube[0][2][1] = old_faces[1]
    old_cube[0][2][2] = old_faces[2]

    old_cube[5][0][0] = old_faces[11]
    old_cube[5][1][0] = old_faces[10]
    old_cube[5][2][0] = old_faces[9]

    old_cube[1][0][0] = old_faces[5]
    old_cube[1][0][1] = old_faces[4]
    old_cube[1][0][2] = old_faces[3]

    old_cube[4][0][2] = old_faces[8]
    old_cube[4][1][2] = old_faces[7]
    old_cube[4][2][2] = old_faces[6]

    return old_cube

def move_B_clockwise(old_cube):
    old_faces = [
        old_cube[0][0][0], old_cube[0][0][1], old_cube[0][0][2],
        old_cube[1][2][0], old_cube[1][2][1], old_cube[1][2][2],
        old_cube[4][0][0], old_cube[4][1][0], old_cube[4][2][0],
        old_cube[5][0][2], old_cube[5][1][2], old_cube[5][2][2] 
    ]

    old_cube[3] = rotate_clockwise2D(old_cube[3])

    old_cube[0][0][0] = old_faces[9] 
    old_cube[0][0][1] = old_faces[10]
    old_cube[0][0][2] = old_faces[11]

    old_cube[1][2][0] = old_faces[6] 
    old_cube[1][2][1] = old_faces[7]
    old_cube[1][2][2] = old_faces[8]

    old_cube[4][0][0] = old_faces[2] 
    old_cube[4][1][0] = old_faces[1]
    old_cube[4][2][0] = old_faces[0]

    old_cube[5][0][2] = old_faces[5] 
    old_cube[5][1][2] = old_faces[4]
    old_cube[5][2][2] = old_faces[3]

    return old_cube

def move_B_counterclockwise(old_cube):
    old_faces = [
        old_cube[0][0][0], old_cube[0][0][1], old_cube[0][0][2], # up 
        old_cube[5][0][2], old_cube[5][1][2], old_cube[5][2][2], # right 
        old_cube[1][2][0], old_cube[1][2][1], old_cube[1][2][2], # down
        old_cube[4][0][0], old_cube[4][1][0], old_cube[4][2][0]  # left
    ]

    old_cube[3] = rotate_counterclockwise2D(old_cube[3])

    old_cube[5][0][2] = old_faces[0]
    old_cube[5][1][2] = old_faces[1]
    old_cube[5][2][2] = old_faces[2]

    old_cube[1][2][0] = old_faces[5]
    old_cube[1][2][1] = old_faces[4]
    old_cube[1][2][2] = old_faces[3]

    old_cube[4][0][0] = old_faces[6]
    old_cube[4][1][0] = old_faces[7]
    old_cube[4][2][0] = old_faces[8]

    old_cube[0][0][0] = old_faces[11]
    old_cube[0][0][1] = old_faces[10]
    old_cube[0][0][2] = old_faces[9]

    return old_cube

original_cube = copy.deepcopy(cube)
move_B_counterclockwise(cube)
move_B_clockwise(cube)
print(original_cube == cube)