# in-triang-mesh

This repository contains a python package to install the `in-triang-mesh` tool for checking whether or not a point in 3D Cartesian space lies within a triangular mesh defined by a given .stl file. This is accomplished by solving for the winding number of the closed triangular mesh with respect to the given point as outlined in [[1]](#1).

## Environment Setup

The following commands should be run from the root directory of the package.

Setup and start a python virtual environment:
```
$> python3 -v venv venv
$> source venv/bin/activate
```
Install the third party packages requirements:
```
$> pip install -r requirements.txt
```
Install the package in developer mode:
```
$> pip install -e .
```

## Usage
The package will install an executable that can be called as follows:
```
$> in-triang-mesh --help
usage: in-triang-mesh [-h] [--plot] [--point POINT POINT POINT] file_path

Tool to plot a triangular mesh from a .stl or check if a point lies within a .stl file. If a point is not given and the plot option is not passed the tool will default to plotting the given .stl.

positional arguments:
  file_path             A valid path to a .stl file.

optional arguments:
  -h, --help            show this help message and exit
  --plot                Plot the .stl file.
  --point x y z         Check if a given 3D point in Cartesian space is within given triangular mesh. This argument expects to be followed by three floats representing (x y z) the point.
```
Example:
```
$> in-triang-mesh path/to/valid.stl --plot --point 1 2 3
```

## Testing

Run the tests from the root of the package directory with `pytest`:
```
$> pytest -v
```

## References
<a id="1">[1]</a>
Jacobson, Alec & Kavan, Ladislav & Sorkine-Hornung, Olga. (2013). [Robust Inside-Outside Segmentation Using Generalized Winding Numbers.](https://igl.ethz.ch/projects/winding-number/robust-inside-outside-segmentation-using-generalized-winding-numbers-siggraph-2013-jacobson-et-al.pdf) ACM Transactions on Graphics (TOG). 32. 10.1145/2461912.2461916.