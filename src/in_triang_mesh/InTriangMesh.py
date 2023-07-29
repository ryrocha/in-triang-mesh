"""
File: src/in_triang_mesh/InTriangMesh.py

Description:
	This file contains a class that can be used to do the following:
		- Create a 3D plot of a triangular mesh from a .stl file
		- Check if a 3D point lies within a triangular mesh from a .stl file
"""

from typing import List

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from stl import mesh


class InTriangMesh:
	"""Checks whether or not a point lies within a triangular mesh.

	This class is also capable of plotting the triangular mesh that it is
	initialized with.

	Usage:
		obj = InTriangMesh("path/to/valid.stl")
		obj.plot_mesh()
		obj.in_triang_mesh([10, 20, 30])
	"""

	def __init__(self, stl_file: str) -> None:
		"""Initializes the object given the path to a .stl file.

		Args:
			stl_file (str): This should be a valid path to a .stl file.
		"""
		self._mesh = mesh.Mesh.from_file(stl_file)

	def plot_mesh(self) -> None:
		"""Plot the 3D mesh associated with this object."""
		figure = plt.figure()
		axes = figure.add_subplot(projection="3d")

		axes.add_collection3d(
			mplot3d.art3d.Poly3DCollection(self._mesh.vectors, edgecolor="k")
		)
		scale = self._mesh.points.flatten()
		axes.auto_scale_xyz(scale, scale, scale)

		plt.show()

	def in_triang_mesh(self, point: List[float]) -> bool:
		"""Returns a bool indicating whether or not a point is within the mesh.

		Args:
			point (List[float]): [x, y, z] of a point in the three-dimensional
				Cartesian coordinate system of the associated mesh

		Returns:
			bool: True if the point lies within the triangular mesh, False
				if otherwise.
		"""
		aa = np.subtract(self._mesh.v0, point)
		bb = np.subtract(self._mesh.v1, point)
		cc = np.subtract(self._mesh.v2, point)

		det = np.linalg.det(np.stack((aa, bb, cc), axis=-1))

		a_dot_b = np.einsum("ij,ij->i", aa, bb)
		b_dot_c = np.einsum("ij,ij->i", bb, cc)
		c_dot_a = np.einsum("ij,ij->i", cc, aa)

		a_norm = np.linalg.norm(aa, axis=1)
		b_norm = np.linalg.norm(bb, axis=1)
		c_norm = np.linalg.norm(cc, axis=1)

		abc = a_norm * b_norm * c_norm
		divisor = abc + (a_dot_b) * c_norm + (b_dot_c) * a_norm + (c_dot_a) * b_norm
		solid_angle = 2 * np.arctan(det / divisor)
		return int(np.sum(solid_angle / (4 * np.pi))) != 0
