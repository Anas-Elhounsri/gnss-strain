from setuptools import setup, find_packages

setup(
    name="gnss-strain",
    version="1.0.0",
    description="Strain-rate estimation from GNSS velocity fields",
    author="Lucia Moreno",
    author_email="lucia.moreno@example.org",
    packages=find_packages(),
    install_requires=["numpy>=1.24.0", "scipy>=1.10.0", "pandas>=2.0.0"],
)
