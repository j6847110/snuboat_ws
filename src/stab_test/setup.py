from setuptools import find_packages
from setuptools import setup

package_name = 'stab_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='minsung',
    maintainer_email='minsung@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'str = stab_test.str:main',
        'turn_pt = stab_test.turning:turn_pt',
        'turn_st = stab_test.turning:turn_st',
        ],
    },
)
