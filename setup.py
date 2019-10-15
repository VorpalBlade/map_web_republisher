## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['map_web_republisher'],
    package_dir={'': 'src'},
    install_requires=['numpy>=1.11,<1.12', 'imageio', 'pillow>=6.2.0', 'pathlib2'],
)

setup(**setup_args)
