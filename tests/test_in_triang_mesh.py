"""
File: tests/test_in_triang_mesh.py

Description:
	This file contains unit tests around the functionality of the InTriangMesh
	object.
"""

import os

from in_triang_mesh.InTriangMesh import InTriangMesh


def get_stl_path(stl_name: str) -> str:
	"""Get the path to a specific .stl file in the testing directory.

	Args:
		stl_name (str): The name of the .stl file for which to generate the path.

	Returns:
		str: The path to the desired .stl file.
	"""
	tests_dir = os.path.dirname(os.path.realpath(__file__))
	return os.path.join(tests_dir, "stl_files", f"{stl_name}.stl")


def test_in_hollow_cube():
	obj = InTriangMesh(get_stl_path("hollow_cube"))
	assert obj.in_triang_mesh([1, 2, 3])


def test_outside_hollow_cube():
	obj = InTriangMesh(get_stl_path("hollow_cube"))
	assert not obj.in_triang_mesh([20, 20, 20])


def test_in_spring():
	obj = InTriangMesh(get_stl_path("spring"))
	assert obj.in_triang_mesh([9, 0, 30])


def test_outside_spring():
	obj = InTriangMesh(get_stl_path("spring"))
	assert not obj.in_triang_mesh([0, 0, 20])
