# import bpy

# define vertices and faces for a cube

directions = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

def coordinates_from_direction((x,y,z)):
    print(x)

coordinates_from_direction(directions[0])







# coords=[ (-1,-1,-1), (1,-1,-1), (1,1,-1), (-1,1,-1), (-1,-1,1), (1,-1,1), (1,1,1), (-1,1,1) ]
# faces= [ (0,1,2,3), (4,5,6,7), (0,1,5,4), (1,2,6,5), (2,3,7,6), (3,0,4,7) ]
#
# mesh = bpy.data.meshes.new('TriangleCube')          # create a new mesh
# object = bpy.data.objects.new('TrinagleCube', mesh)
#
# object.location = bpy.context.scene.cursor_location
# bpy.context.scene.objects.link(object)
#
# mesh.from_pydata(coords, [], faces)
# mesh.update(calc_edges=True)
