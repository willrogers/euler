'''
Find the second-smallest triangle number which is also 
pentagonal and hexagonal.
'''

from utils import triangles, is_tri, is_pen, is_hex



for tri in triangles():
    if not is_tri(tri):
        print("wtf?")
        sys.exit()
    if is_pen(tri):
        if is_hex(tri):
            print("found! %s" % tri)



