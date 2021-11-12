import cube

def F(num):
    for i in range(num):
        tempo = [cube.cube_state["left"][8], cube.cube_state["left"][5], cube.cube_state["left"][2]]
        tempw = [cube.cube_state["up"][6], cube.cube_state["up"][7], cube.cube_state["up"][8]]
        tempr = [cube.cube_state["right"][0], cube.cube_state["right"][3], cube.cube_state["right"][6]]
        tempy = [cube.cube_state["down"][2], cube.cube_state["down"][1], cube.cube_state["down"][0]]
        
        tempw, tempr, tempy, tempo = tempo, tempw, tempr, tempy
        
        [cube.cube_state["left"][8], cube.cube_state["left"][5], cube.cube_state["left"][2]] = tempo[0], tempo[1], tempo[2]
        [cube.cube_state["up"][6], cube.cube_state["up"][7], cube.cube_state["up"][8]] = tempw[0], tempw[1], tempw[2]
        [cube.cube_state["right"][0], cube.cube_state["right"][3], cube.cube_state["right"][6]] = tempr[0], tempr[1], tempr[2]
        [cube.cube_state["down"][2], cube.cube_state["down"][1], cube.cube_state["down"][0]] = tempy[0], tempy[1], tempy[2]
        
        face = "front"
        tempg = [cube.cube_state[face][0], cube.cube_state[face][1], cube.cube_state[face][2], cube.cube_state[face][3], cube.cube_state[face][5], cube.cube_state[face][6], cube.cube_state[face][7], cube.cube_state[face][8]]
        [cube.cube_state[face][2], cube.cube_state[face][5], cube.cube_state[face][8], cube.cube_state[face][1], cube.cube_state[face][7], cube.cube_state[face][0], cube.cube_state[face][3], cube.cube_state[face][6]] = tempg

def U(num):
    for i in range(num):
        tempg = [cube.cube_state["front"][2], cube.cube_state["front"][1], cube.cube_state["front"][0]]
        tempo = [cube.cube_state["left"][2], cube.cube_state["left"][1], cube.cube_state["left"][0]]
        tempb = [cube.cube_state["back"][2], cube.cube_state["back"][1], cube.cube_state["back"][0]]
        tempr = [cube.cube_state["right"][2], cube.cube_state["right"][1], cube.cube_state["right"][0]]
        
        tempo, tempb, tempr, tempg = tempg, tempo, tempb, tempr
        
        [cube.cube_state["front"][2], cube.cube_state["front"][1], cube.cube_state["front"][0]] = tempg[0], tempg[1], tempg[2]
        [cube.cube_state["left"][2], cube.cube_state["left"][1], cube.cube_state["left"][0]] = tempo[0], tempo[1], tempo[2]
        [cube.cube_state["back"][2], cube.cube_state["back"][1], cube.cube_state["back"][0]] = tempb[0], tempb[1], tempb[2]
        [cube.cube_state["right"][2], cube.cube_state["right"][1], cube.cube_state["right"][0]] = tempr[0], tempr[1], tempr[2]
        
        face = "up"
        tempw = [cube.cube_state[face][0], cube.cube_state[face][1], cube.cube_state[face][2], cube.cube_state[face][3], cube.cube_state[face][5], cube.cube_state[face][6], cube.cube_state[face][7], cube.cube_state[face][8]]
        [cube.cube_state[face][2], cube.cube_state[face][5], cube.cube_state[face][8], cube.cube_state[face][1], cube.cube_state[face][7], cube.cube_state[face][0], cube.cube_state[face][3], cube.cube_state[face][6]] = tempw

        
def R(num):
    for i in range(num):
        tempg = [cube.cube_state["front"][8], cube.cube_state["front"][5], cube.cube_state["front"][2]]
        tempw = [cube.cube_state["up"][8], cube.cube_state["up"][5], cube.cube_state["up"][2]]
        tempb = [cube.cube_state["back"][0], cube.cube_state["back"][3], cube.cube_state["back"][6]]
        tempy = [cube.cube_state["down"][8], cube.cube_state["down"][5], cube.cube_state["down"][2]]
        
        tempw, tempb, tempy, tempg = tempg, tempw, tempb, tempy
        
        cube.cube_state["front"][8], cube.cube_state["front"][5], cube.cube_state["front"][2] = tempg[0], tempg[1], tempg[2]
        cube.cube_state["up"][8], cube.cube_state["up"][5], cube.cube_state["up"][2] = tempw[0], tempw[1], tempw[2]
        cube.cube_state["back"][0], cube.cube_state["back"][3], cube.cube_state["back"][6] = tempb[0], tempb[1], tempb[2]
        cube.cube_state["down"][8], cube.cube_state["down"][5], cube.cube_state["down"][2] = tempy[0], tempy[1], tempy[2]
        
        face = "right"
        tempr = [cube.cube_state[face][0], cube.cube_state[face][1], cube.cube_state[face][2], cube.cube_state[face][3], cube.cube_state[face][5], cube.cube_state[face][6], cube.cube_state[face][7], cube.cube_state[face][8]]
        [cube.cube_state[face][2], cube.cube_state[face][5], cube.cube_state[face][8], cube.cube_state[face][1], cube.cube_state[face][7], cube.cube_state[face][0], cube.cube_state[face][3], cube.cube_state[face][6]] = tempr


def D(num):
    for i in range(num):        
        tempg = [cube.cube_state["front"][6], cube.cube_state["front"][7], cube.cube_state["front"][8]]
        tempo = [cube.cube_state["left"][6], cube.cube_state["left"][7], cube.cube_state["left"][8]]
        tempb = [cube.cube_state["back"][6], cube.cube_state["back"][7], cube.cube_state["back"][8]]
        tempr = [cube.cube_state["right"][6], cube.cube_state["right"][7], cube.cube_state["right"][8]]
        
        tempr, tempg, tempo, tempb = tempg, tempo, tempb, tempr
        
        [cube.cube_state["front"][6], cube.cube_state["front"][7], cube.cube_state["front"][8]] = tempg[0], tempg[1], tempg[2]
        [cube.cube_state["left"][6], cube.cube_state["left"][7], cube.cube_state["left"][8]] = tempo[0], tempo[1], tempo[2]
        [cube.cube_state["back"][6], cube.cube_state["back"][7], cube.cube_state["back"][8]] = tempb[0], tempb[1], tempb[2]
        [cube.cube_state["right"][6], cube.cube_state["right"][7], cube.cube_state["right"][8]] = tempr[0], tempr[1], tempr[2]
        
        face = "down"
        tempy = [cube.cube_state[face][0], cube.cube_state[face][1], cube.cube_state[face][2], cube.cube_state[face][3], cube.cube_state[face][5], cube.cube_state[face][6], cube.cube_state[face][7], cube.cube_state[face][8]]
        [cube.cube_state[face][2], cube.cube_state[face][5], cube.cube_state[face][8], cube.cube_state[face][1], cube.cube_state[face][7], cube.cube_state[face][0], cube.cube_state[face][3], cube.cube_state[face][6]] = tempy

def B(num):
    for i in range(num):        
        tempo = [cube.cube_state["left"][0], cube.cube_state["left"][3], cube.cube_state["left"][6]]
        tempw = [cube.cube_state["up"][2], cube.cube_state["up"][1], cube.cube_state["up"][0]]
        tempr = [cube.cube_state["right"][8], cube.cube_state["right"][5], cube.cube_state["right"][2]]
        tempy = [cube.cube_state["down"][6], cube.cube_state["down"][7], cube.cube_state["down"][8]]
        
        tempy, tempo, tempw, tempr = tempo, tempw, tempr, tempy
        
        [cube.cube_state["left"][0], cube.cube_state["left"][3], cube.cube_state["left"][6]] = tempo[0], tempo[1], tempo[2]
        [cube.cube_state["up"][2], cube.cube_state["up"][1], cube.cube_state["up"][0]] = tempw[0], tempw[1], tempw[2]
        [cube.cube_state["right"][8], cube.cube_state["right"][5], cube.cube_state["right"][2]] = tempr[0], tempr[1], tempr[2]
        [cube.cube_state["down"][6], cube.cube_state["down"][7], cube.cube_state["down"][8]] = tempy[0], tempy[1], tempy[2]
        
        face = "back"
        tempb = [cube.cube_state[face][0], cube.cube_state[face][1], cube.cube_state[face][2], cube.cube_state[face][3], cube.cube_state[face][5], cube.cube_state[face][6], cube.cube_state[face][7], cube.cube_state[face][8]]
        [cube.cube_state[face][2], cube.cube_state[face][5], cube.cube_state[face][8], cube.cube_state[face][1], cube.cube_state[face][7], cube.cube_state[face][0], cube.cube_state[face][3], cube.cube_state[face][6]] = tempb

def L(num):
    for i in range(num):        
        tempg = [cube.cube_state["front"][0], cube.cube_state["front"][3], cube.cube_state["front"][6]]
        tempw = [cube.cube_state["up"][0], cube.cube_state["up"][3], cube.cube_state["up"][6]]
        tempb = [cube.cube_state["back"][8], cube.cube_state["back"][5], cube.cube_state["back"][2]]
        tempy = [cube.cube_state["down"][0], cube.cube_state["down"][3], cube.cube_state["down"][6]]
        
        tempw, tempb, tempy, tempg = tempb, tempy, tempg, tempw
        
        cube.cube_state["front"][0], cube.cube_state["front"][3], cube.cube_state["front"][6] = tempg[0], tempg[1], tempg[2]
        cube.cube_state["up"][0], cube.cube_state["up"][3], cube.cube_state["up"][6] = tempw[0], tempw[1], tempw[2]
        cube.cube_state["back"][8], cube.cube_state["back"][5], cube.cube_state["back"][2] = tempb[0], tempb[1], tempb[2]
        cube.cube_state["down"][0], cube.cube_state["down"][3], cube.cube_state["down"][6] = tempy[0], tempy[1], tempy[2]
        
        face = "left"
        tempo = [cube.cube_state[face][0], cube.cube_state[face][1], cube.cube_state[face][2], cube.cube_state[face][3], cube.cube_state[face][5], cube.cube_state[face][6], cube.cube_state[face][7], cube.cube_state[face][8]]
        [cube.cube_state[face][2], cube.cube_state[face][5], cube.cube_state[face][8], cube.cube_state[face][1], cube.cube_state[face][7], cube.cube_state[face][0], cube.cube_state[face][3], cube.cube_state[face][6]] = tempo