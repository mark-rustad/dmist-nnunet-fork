from setuptools import setup, find_packages

setup(
    name="nnunetv2",
    version="0.1",
    # packages=find_packages(include=["nnunetv2*", "dmist_nnunet*"]),  # Explicitly include your packages
    packages=find_packages(include=["nnunetv2*"]),  # Explicitly include your packages
    # Add other necessary metadata
)
