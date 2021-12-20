import cube
import visualizer


def F(num):
    for i in range(num):
        tempo = [visualizer.state["left"][8], visualizer.state["left"][5], visualizer.state["left"][2]]
        tempw = [visualizer.state["up"][6], visualizer.state["up"][7], visualizer.state["up"][8]]
        tempr = [visualizer.state["right"][0], visualizer.state["right"][3], visualizer.state["right"][6]]
        tempy = [visualizer.state["down"][2], visualizer.state["down"][1], visualizer.state["down"][0]]
        
        tempw, tempr, tempy, tempo = tempo, tempw, tempr, tempy
        
        [visualizer.state["left"][8], visualizer.state["left"][5], visualizer.state["left"][2]] = tempo[0], tempo[1], tempo[2]
        [visualizer.state["up"][6], visualizer.state["up"][7], visualizer.state["up"][8]] = tempw[0], tempw[1], tempw[2]
        [visualizer.state["right"][0], visualizer.state["right"][3], visualizer.state["right"][6]] = tempr[0], tempr[1], tempr[2]
        [visualizer.state["down"][2], visualizer.state["down"][1], visualizer.state["down"][0]] = tempy[0], tempy[1], tempy[2]
        
        face = "front"
        tempg = [visualizer.state[face][0], visualizer.state[face][1], visualizer.state[face][2], visualizer.state[face][3], visualizer.state[face][5], visualizer.state[face][6], visualizer.state[face][7], visualizer.state[face][8]]
        [visualizer.state[face][2], visualizer.state[face][5], visualizer.state[face][8], visualizer.state[face][1], visualizer.state[face][7], visualizer.state[face][0], visualizer.state[face][3], visualizer.state[face][6]] = tempg

def U(num):
    for i in range(num):
        tempg = [visualizer.state["front"][2], visualizer.state["front"][1], visualizer.state["front"][0]]
        tempo = [visualizer.state["left"][2], visualizer.state["left"][1], visualizer.state["left"][0]]
        tempb = [visualizer.state["back"][2], visualizer.state["back"][1], visualizer.state["back"][0]]
        tempr = [visualizer.state["right"][2], visualizer.state["right"][1], visualizer.state["right"][0]]
        
        tempo, tempb, tempr, tempg = tempg, tempo, tempb, tempr
        
        [visualizer.state["front"][2], visualizer.state["front"][1], visualizer.state["front"][0]] = tempg[0], tempg[1], tempg[2]
        [visualizer.state["left"][2], visualizer.state["left"][1], visualizer.state["left"][0]] = tempo[0], tempo[1], tempo[2]
        [visualizer.state["back"][2], visualizer.state["back"][1], visualizer.state["back"][0]] = tempb[0], tempb[1], tempb[2]
        [visualizer.state["right"][2], visualizer.state["right"][1], visualizer.state["right"][0]] = tempr[0], tempr[1], tempr[2]
        
        face = "up"
        tempw = [visualizer.state[face][0], visualizer.state[face][1], visualizer.state[face][2], visualizer.state[face][3], visualizer.state[face][5], visualizer.state[face][6], visualizer.state[face][7], visualizer.state[face][8]]
        [visualizer.state[face][2], visualizer.state[face][5], visualizer.state[face][8], visualizer.state[face][1], visualizer.state[face][7], visualizer.state[face][0], visualizer.state[face][3], visualizer.state[face][6]] = tempw

        
def R(num):
    for i in range(num):
        tempg = [visualizer.state["front"][8], visualizer.state["front"][5], visualizer.state["front"][2]]
        tempw = [visualizer.state["up"][8], visualizer.state["up"][5], visualizer.state["up"][2]]
        tempb = [visualizer.state["back"][0], visualizer.state["back"][3], visualizer.state["back"][6]]
        tempy = [visualizer.state["down"][8], visualizer.state["down"][5], visualizer.state["down"][2]]
        
        tempw, tempb, tempy, tempg = tempg, tempw, tempb, tempy
        
        visualizer.state["front"][8], visualizer.state["front"][5], visualizer.state["front"][2] = tempg[0], tempg[1], tempg[2]
        visualizer.state["up"][8], visualizer.state["up"][5], visualizer.state["up"][2] = tempw[0], tempw[1], tempw[2]
        visualizer.state["back"][0], visualizer.state["back"][3], visualizer.state["back"][6] = tempb[0], tempb[1], tempb[2]
        visualizer.state["down"][8], visualizer.state["down"][5], visualizer.state["down"][2] = tempy[0], tempy[1], tempy[2]
        
        face = "right"
        tempr = [visualizer.state[face][0], visualizer.state[face][1], visualizer.state[face][2], visualizer.state[face][3], visualizer.state[face][5], visualizer.state[face][6], visualizer.state[face][7], visualizer.state[face][8]]
        [visualizer.state[face][2], visualizer.state[face][5], visualizer.state[face][8], visualizer.state[face][1], visualizer.state[face][7], visualizer.state[face][0], visualizer.state[face][3], visualizer.state[face][6]] = tempr


def D(num):
    for i in range(num):        
        tempg = [visualizer.state["front"][6], visualizer.state["front"][7], visualizer.state["front"][8]]
        tempo = [visualizer.state["left"][6], visualizer.state["left"][7], visualizer.state["left"][8]]
        tempb = [visualizer.state["back"][6], visualizer.state["back"][7], visualizer.state["back"][8]]
        tempr = [visualizer.state["right"][6], visualizer.state["right"][7], visualizer.state["right"][8]]
        
        tempr, tempg, tempo, tempb = tempg, tempo, tempb, tempr
        
        [visualizer.state["front"][6], visualizer.state["front"][7], visualizer.state["front"][8]] = tempg[0], tempg[1], tempg[2]
        [visualizer.state["left"][6], visualizer.state["left"][7], visualizer.state["left"][8]] = tempo[0], tempo[1], tempo[2]
        [visualizer.state["back"][6], visualizer.state["back"][7], visualizer.state["back"][8]] = tempb[0], tempb[1], tempb[2]
        [visualizer.state["right"][6], visualizer.state["right"][7], visualizer.state["right"][8]] = tempr[0], tempr[1], tempr[2]
        
        face = "down"
        tempy = [visualizer.state[face][0], visualizer.state[face][1], visualizer.state[face][2], visualizer.state[face][3], visualizer.state[face][5], visualizer.state[face][6], visualizer.state[face][7], visualizer.state[face][8]]
        [visualizer.state[face][2], visualizer.state[face][5], visualizer.state[face][8], visualizer.state[face][1], visualizer.state[face][7], visualizer.state[face][0], visualizer.state[face][3], visualizer.state[face][6]] = tempy

def B(num):
    for i in range(num):        
        tempo = [visualizer.state["left"][0], visualizer.state["left"][3], visualizer.state["left"][6]]
        tempw = [visualizer.state["up"][2], visualizer.state["up"][1], visualizer.state["up"][0]]
        tempr = [visualizer.state["right"][8], visualizer.state["right"][5], visualizer.state["right"][2]]
        tempy = [visualizer.state["down"][6], visualizer.state["down"][7], visualizer.state["down"][8]]
        
        tempy, tempo, tempw, tempr = tempo, tempw, tempr, tempy
        
        [visualizer.state["left"][0], visualizer.state["left"][3], visualizer.state["left"][6]] = tempo[0], tempo[1], tempo[2]
        [visualizer.state["up"][2], visualizer.state["up"][1], visualizer.state["up"][0]] = tempw[0], tempw[1], tempw[2]
        [visualizer.state["right"][8], visualizer.state["right"][5], visualizer.state["right"][2]] = tempr[0], tempr[1], tempr[2]
        [visualizer.state["down"][6], visualizer.state["down"][7], visualizer.state["down"][8]] = tempy[0], tempy[1], tempy[2]
        
        face = "back"
        tempb = [visualizer.state[face][0], visualizer.state[face][1], visualizer.state[face][2], visualizer.state[face][3], visualizer.state[face][5], visualizer.state[face][6], visualizer.state[face][7], visualizer.state[face][8]]
        [visualizer.state[face][2], visualizer.state[face][5], visualizer.state[face][8], visualizer.state[face][1], visualizer.state[face][7], visualizer.state[face][0], visualizer.state[face][3], visualizer.state[face][6]] = tempb

def L(num):
    for i in range(num):        
        tempg = [visualizer.state["front"][0], visualizer.state["front"][3], visualizer.state["front"][6]]
        tempw = [visualizer.state["up"][0], visualizer.state["up"][3], visualizer.state["up"][6]]
        tempb = [visualizer.state["back"][8], visualizer.state["back"][5], visualizer.state["back"][2]]
        tempy = [visualizer.state["down"][0], visualizer.state["down"][3], visualizer.state["down"][6]]
        
        tempw, tempb, tempy, tempg = tempb, tempy, tempg, tempw
        
        visualizer.state["front"][0], visualizer.state["front"][3], visualizer.state["front"][6] = tempg[0], tempg[1], tempg[2]
        visualizer.state["up"][0], visualizer.state["up"][3], visualizer.state["up"][6] = tempw[0], tempw[1], tempw[2]
        visualizer.state["back"][8], visualizer.state["back"][5], visualizer.state["back"][2] = tempb[0], tempb[1], tempb[2]
        visualizer.state["down"][0], visualizer.state["down"][3], visualizer.state["down"][6] = tempy[0], tempy[1], tempy[2]
        
        face = "left"
        tempo = [visualizer.state[face][0], visualizer.state[face][1], visualizer.state[face][2], visualizer.state[face][3], visualizer.state[face][5], visualizer.state[face][6], visualizer.state[face][7], visualizer.state[face][8]]
        [visualizer.state[face][2], visualizer.state[face][5], visualizer.state[face][8], visualizer.state[face][1], visualizer.state[face][7], visualizer.state[face][0], visualizer.state[face][3], visualizer.state[face][6]] = tempo