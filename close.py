import pyvista as pv

def is_closed_surface(mesh):
    # Check if the mesh is closed by verifying that it contains only a single connected component.
    return len(mesh.extract_largest_component().n_cells) == mesh.n_cells

def main(input_file):
    try:
        mesh = pv.read(input_file)  # Load the 3D model

        if is_closed_surface(mesh):
            print("The 3D model is a closed surface.")
        else:
            print("The 3D model is an open surface.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_file = "unit_surf_4.obj"  # Replace with the path to your 3D model file (e.g., .stl)
    main(input_file)
