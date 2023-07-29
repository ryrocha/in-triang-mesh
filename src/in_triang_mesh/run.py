"""
File: src/in_triang_mesh/run.py

Description:
	This file contains methods for taking user inputs from a command line,
	parsing those inputs and calling InTriangMesh accordingly.
"""

import argparse
import sys

from in_triang_mesh.InTriangMesh import InTriangMesh


def setup_opts() -> argparse.Namespace:
	"""Helper function for setting up a command line option parser.

	Returns:
		argparse.Namespace: The arguements passed in from the command line by
			the user.
	"""
	parser = argparse.ArgumentParser(
		description=(
			"Tool to plot a triangular mesh from a .stl or check if a \
			point lies within a .stl file. If a point is not given and \
			the plot option is not passed the tool will default to plotting \
			the given .stl."
		)
	)
	parser.add_argument(
		"file_path",
		help=("A valid path to a .stl file."),
	)
	parser.add_argument(
		"--plot",
		action="store_true",
		help=("Plot the .stl file."),
	)
	parser.add_argument(
		"--point",
		nargs=3,
		type=float,
		metavar=("x", "y", "z"),
		help=(
			"Check if a given 3D point in Cartesian space is within the given \
			triangular mesh. This argument expects to be followed by three \
			floats representing (x y z) the point."
		),
	)

	opts = parser.parse_args()
	return opts


def main() -> None:
	"""Function to call InTriangMesh according to a user's command line input."""
	opts = setup_opts()
	obj = InTriangMesh(opts.file_path)

	exit_code = 0
	if opts.point:
		in_mesh = obj.in_triang_mesh(opts.point)
		if in_mesh:
			print(
				f"Point {opts.point} is in {opts.file_path}"
			)
		else:
			print(
				f"Point {opts.point} is outside of {opts.file_path}"
			)
			exit_code = 1

	if opts.plot or (not opts.plot and opts.point is None):
		obj.plot_mesh()

	sys.exit(exit_code)


if __name__ == "__main__":
	main()
