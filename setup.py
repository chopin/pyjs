from setuptools import setup
import setup_pyjstools
import setup_pyjswidgets
import setup_pyjd
__VERSION__='0.8.1'

packages=setup_pyjstools.packages+setup_pyjswidgets.packages+setup_pyjd.packages
package_data=dict(setup_pyjstools.package_data.items()+setup_pyjswidgets.package_data.items()+setup_pyjd.package_data.items())
entry_points=dict(setup_pyjstools.entry_points.items()+setup_pyjswidgets.entry_points.items()+setup_pyjd.entry_points.items())

setup(
    name="pyjs",
    version=__VERSION__,
    packages=packages,
    package_data=package_data,
    zip_safe = False,
    entry_points = entry_points,
    )
