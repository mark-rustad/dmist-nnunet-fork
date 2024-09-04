from setuptools import setup, find_packages

setup(
    name='nnunet',
    version='0.1',
    packages=find_packages(include=['nnunetv2*', 'scripts_mdr*']),  # Explicitly include your packages
    # Add other necessary metadata
)