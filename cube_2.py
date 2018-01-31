import bpy

# cube has 6 faces directions
directions = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
# each face has 4 squares
vertices = [(1,1),(1,-1),(-1,-1),(-1,1)]

# from each face direction we create 4 coordinates by combining them with squares
def coordinates_from_direction(tuple_xyz):
    (x,y,z) = tuple_xyz
    if x!=0:
      return [(x,vertices[0][0],vertices[0][1]),
              (x,vertices[1][0],vertices[1][1]),
              (x,vertices[2][0],vertices[2][1]),
              (x,vertices[3][0],vertices[3][1]),]
    elif y!=0:
      return [(vertices[0][0],y,vertices[0][1]),
              (vertices[1][0],y,vertices[1][1]),
              (vertices[2][0],y,vertices[2][1]),
              (vertices[3][0],y,vertices[3][1]),]
    else: # z!=0
      return [(vertices[0][0],vertices[0][1],z),
              (vertices[1][0],vertices[1][1],z),
              (vertices[2][0],vertices[2][1],z),
              (vertices[3][0],vertices[3][1],z),]

# we create the whole list of coordinates
def create_coordinate_list():
    coordinates = []
    for direction in directions:
        temp_coordinate = coordinates_from_direction(direction)
        coordinates.extend(temp_coordinate)
    return coordinates

coordinates = create_coordinate_list()
faces_list = list(range(0,24))
faces_iter = iter(faces_list)
faces = list(zip(faces_iter,faces_iter,faces_iter,faces_iter))
print(coordinates)
print(faces)

mesh = bpy.data.meshes.new('TriangleCube')          # create a new mesh
object = bpy.data.objects.new('TriangleCubeName', mesh)

object.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(object)

mesh.from_pydata(coordinates, [], faces)
mesh.update(calc_edges=True)
