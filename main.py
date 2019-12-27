# import sys
# sys.path.insert(0, './libs')

# import helper

# def render():
#     print(helper.greeting('Tiffany','Hudgens'))



# render()



# import sys
# sys.path.insert(0, './libs')
# from helper import greeting

# def render():
#     print(greeting('Tiffany','Hudgens'))


# render()



# Alias assigned on import of module

import sys
sys.path.insert(0, './libs')
import helper as h

def render():
    print(h.greeting('Tiffany','Hudgens'))


render()

import math as m

m.sqrt(4)
