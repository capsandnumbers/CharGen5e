from setuptools import setup, find_packages

setup(
    name="CharGen5e",  # Name of the package
    version="0.1.0",          # Version number
    description="A D&D character generator with race, class, and background logic.",
    author="Your Name",
    packages=find_packages(),  # Automatically finds `dndCharGenerator` and its subpackages
    install_requires=[         # Add any external libraries you use here
        "numpy",
        "pdfrw"              # Example: dependency for PDF handling
    ],
    python_requires=">=3.7",   # Minimum Python version
)
