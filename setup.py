"""
File: setup.py

Description:
	This file is used to build the in-traing-mesh package.
"""

from setuptools import find_packages, setup

requirements = [
	"numpy",
	"matplotlib",
	"numpy-stl",
]

test_requirements = [
	"pytest",
]

with open("README.md", "r", encoding="utf-8") as f:
	long_description = f.read()

setup(
	name="in-triang-mesh",
	description="A tool for checking if a point lies within a 3D triangular mesh",
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=find_packages(where="src"),
	package_dir={"": "src"},
	entry_points={"console_scripts": ["in-triang-mesh=in_triang_mesh.run:main"]},
	python_requires=">=3",
	extras_require={"tests": test_requirements},
	install_requires=requirements,
)
