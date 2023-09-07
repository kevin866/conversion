import bpy

# Clear existing objects and mesh data
bpy.ops.wm.read_factory_settings(use_empty=True)

# Load your 3D model (replace 'your_model.obj' with your model's file path)
bpy.ops.import_scene.obj(filepath='unit_surf_4.obj')

# Select the imported object (assuming it's the active object)
imported_object = bpy.context.active_object

# Switch to Edit Mode for mesh operations
bpy.ops.object.mode_set(mode='EDIT')

# Perform mesh repair operations

# Example 1: Remove Doubles (merge duplicate vertices)
bpy.ops.mesh.select_all(action='SELECT')  # Select all vertices
bpy.ops.mesh.remove_doubles(threshold=0.0001)  # Adjust the threshold as needed

# Example 2: Fill Holes (triangulate faces to fill holes)
bpy.ops.mesh.select_all(action='SELECT')  # Select all vertices
bpy.ops.mesh.fill()

# Example 3: Recalculate Normals
bpy.ops.mesh.normals_make_consistent(inside=False)

# Switch back to Object Mode
bpy.ops.object.mode_set(mode='OBJECT')

# Save the repaired model (replace 'repaired_model.obj' with the desired output file path)
bpy.ops.export_scene.obj(filepath='repaired_model.obj', use_selection=True)

# Optional: Quit Blender (uncomment the next line if needed)
# bpy.ops.wm.quit_blender()
