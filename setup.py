from setuptools import find_packages, setup

setup(
    name='kalpas',
    version='0.1.0',
    packages=find_packages(),
    includ_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ]
)
