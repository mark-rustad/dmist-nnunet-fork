from setuptools import setup, find_packages

setup(
    name='nnunet',
    version='0.1',
    packages=find_packages(include=['nnunetv2*', 'irf_scripts*']),  # Explicitly include your packages
    # Add other necessary metadata
)