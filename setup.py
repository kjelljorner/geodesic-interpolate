"""Installer for geodesic interpolation package.
Install the package into python environment, and provide an entry point for the
main interpolation script.

To run the package as standalone
"""
from setuptools import setup
 
setup(
  name='geodesic-interpolate',
  version='1.0.0',
  description='Interpolation and smoothing of reaction paths with geodesics in '
              'redundant internal coordinates.',
  packages=['geodesic_interpolate'],
  install_requires=["numpy", "scipy"],
  python_requires=">=3.8",  
  entry_points = {
    'console_scripts': [
      'geodesic_interpolate=geodesic_interpolate.__main__:main',
    ],
  },
)
