import cube
import moves
import kociemba

def current_state(state):
    raw = ''
    for i in state:
        for j in state[i]:
            raw += cube.sign_conv[j]
    return raw

def solve(state):
    return kociemba.solve(current_state(state))
"""
def process(operation):
    replace = {
        "F":[moves.F, 1],
        "U":[moves.U, 1],
        "R":[moves.R, 1],
        "D":[moves.D, 1],
        "B":[moves.B, 1],
        "L":[moves.L, 1],
        "F2":[moves.F, 2],
        "U2":[moves.U, 2],
        "R2":[moves.R, 2],
        "D2":[moves.D, 2],
        "B2":[moves.B, 2],
        "L2":[moves.L, 2],
        "F'":[moves.F, 3],
        "U'":[moves.U, 3],
        "R'":[moves.R, 3],
        "D'":[moves.D, 3],
        "B'":[moves.B, 3],
        "L'":[moves.L, 3]
    }
    
    for i in operation:
        replace[i][0](replace[i][1])
        #print("\n")
        #print(cube.cube_state)
"""
"""
solution = solve(cube.cube_state)
print(solution)

operation = solution.split(' ')
print(operation)
 
process(operation)
"""