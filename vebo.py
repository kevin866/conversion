import numpy as np
from scipy.spatial import ConvexHull
import tripy
from tripy import Point

# Load the OBJ file
with open("unit_surf_5.obj", "r") as file:
    obj_data = file.read()
    
vertices = []
for line in obj_data.splitlines():
    if line.startswith("v "):
        _, x, y, z = line.split()
        vertices.append(Point(x=float(x), y=float(y)))

vertices = np.array(vertices)
triangles = []
hull = ConvexHull(vertices)
for simplex in hull.simplices:
    triangles.append(vertices[simplex])
voxel_size = 0.01  # Adjust this based on your needs
grid_min = np.min(vertices, axis=0)
grid_max = np.max(vertices, axis=0)

grid_dimensions = np.ceil((grid_max - grid_min) / voxel_size).astype(int)
voxel_grid = np.zeros(grid_dimensions, dtype=bool)
from scipy.spatial import Ray

for x in range(grid_dimensions[0]):
    for y in range(grid_dimensions[1]):
        for z in range(grid_dimensions[2]):
            voxel_center = grid_min + np.array([x, y, z]) * voxel_size + voxel_size / 2
            ray = Ray(voxel_center, np.array([0, 0, 1]))  # Adjust the ray direction as needed

            for triangle in triangles:
                if tripy.intersect(ray, triangle):
                    voxel_grid[x, y, z] = True
                    break
np.save("voxel_grid.npy", voxel_grid)