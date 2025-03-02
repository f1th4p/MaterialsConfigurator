import streamlit as st
import pyvista as pv
from stpyvista import stpyvista

# Load your 3D model
mesh = pv.read('model.glb')

# Create a plotter object
plotter = pv.Plotter()
plotter.add_mesh(mesh)

# Display the plotter in Streamlit
stpyvista(plotter)
