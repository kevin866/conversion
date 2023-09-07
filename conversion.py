import numpy as np
import pyvista as pv
from pyvista import examples
file = 'unit_surf_5.obj'
# Load a surface to voxelize
reader = pv.get_reader('unit_surf_5.obj')
surface = reader.read()
# surface = examples.download_foot_bones()
print(surface)

voxels = pv.voxelize(surface, density=surface.length / 500, check_surface=False)
# Save the voxels to a file (e.g., in VTK format)
output_filename = 'voxels.vtk'  # Change the filename and format as needed
voxels.save(output_filename)

# Optional: You can also save the voxels in other formats like STL or PLY if needed.
# voxels.save('voxels.stl')  # STL format
# voxels.save('voxels.ply')  # PLY format

# Display the voxels
voxels.plot(opacity=1.00)