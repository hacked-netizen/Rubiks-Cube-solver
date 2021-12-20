cube_state = {
    'up': ['blue', 'white', 'blue', 'white', 'white', 'white', 'white', 'green', 'white'], 
    'right': ['blue', 'blue', 'yellow', 'red', 'red', 'red', 'blue', 'blue', 'yellow'], 
    'front': ['red', 'orange', 'red', 'blue', 'green', 'white', 'red', 'orange', 'red'], 
    'down': ['yellow', 'blue', 'yellow', 'yellow', 'yellow', 'yellow', 'green', 'yellow', 'green'], 
    'left': ['white', 'green', 'green', 'red', 'orange', 'red', 'white', 'green', 'green'], 
    'back': ['orange', 'orange', 'orange', 'yellow', 'blue', 'green', 'orange', 'orange', 'orange']
}

"""
state=  {
            'up':['white','white','white','white','white','white','white','white','white',],
            'right':['white','white','white','white','white','white','white','white','white',],
            'front':['white','white','white','white','white','white','white','white','white',],
            'down':['white','white','white','white','white','white','white','white','white',],
            'left':['white','white','white','white','white','white','white','white','white',],
            'back':['white','white','white','white','white','white','white','white','white',]
        }
"""

sign_conv = {
    'white': 'U', 
    'yellow': 'D', 
    'orange': 'L', 
    'red': 'R', 
    'blue': 'B', 
    'green': 'F'
}