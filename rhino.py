import rhino3dm

# Initialize Rhino3dm
rhino3dm.license = "RH70-RB03-HGG4-UH0J-A1VP-846R"  # Replace with your Rhino license key
model = rhino3dm.File3dm()  # Create a new 3DM model

# Import the OBJ file into Rhino3dm
obj_file_path = "unit_surf_5.obj"
success = model.Import(obj_file_path)

if not success:
    print("Failed to import the OBJ file.")
else:
    print("OBJ file imported successfully.")

# Convert the mesh to NURBS surfaces
# This may require additional steps and manual adjustments
# depending on the complexity of the mesh

# Save the model with NURBS surfaces to a 3DM file
output_3dm_file = "output.nurbs.3dm"
model.Write(output_3dm_file)

print(f"Conversion complete. NURBS model saved to {output_3dm_file}")
