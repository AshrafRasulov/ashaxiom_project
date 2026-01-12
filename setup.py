from setuptools import setup, find_packages

# Standard setup configuration for AshAxiom Global Edition
setup(
    name="ashaxiom",
    version="2.4.3",  # Incremented version for the new architecture
    author="Ashraf Rasulov",
    description="Intelligent Math & Financial Framework with Parallel Expert Consilium",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/ashaxiom/",
    packages=find_packages(),
    include_package_data=True, # Critical for including ashaxiom-lesson assets
    package_data={
        'ashaxiom': ['ashaxiom-lesson/**/*'], # Ensures all Academy files are bundled
    },
    install_requires=[
        "numpy", 
        "sympy", 
        "matplotlib", 
        "pandas", 
        "scipy", 
        "yfinance", 
        "statsmodels", 
        "openpyxl"
    ],
    classifiers=[
        "Framework :: Jupyter",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    python_requires='>=3.7',
)