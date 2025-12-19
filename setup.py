from setuptools import setup, find_packages

setup(
    name="ashaxiom",
    version="0.1.0",
    packages=find_packages(),
    description="A high-level mathematical analysis library for Jupyter Notebook designed for advanced calculations and higher mathematics solutions.",
    
    author="Ashraf",
    author_email="your_email@example.com", # Mojesh zamenit' na svoy real'nyy email
    
    # Ispravlennaya ssylka na tvoy GitHub
    url="https://github.com/AshrafRasulov/ashaxiom_project", 
    
    long_description=open("README.md").read() if hasattr(open("README.md"), "read") else "AshAxiom Library",
    long_description_content_type="text/markdown",
    
    install_requires=[
        "numpy",
        "matplotlib",
        "scipy",
        "sympy"
    ],
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Framework :: Jupyter",
    ],
    python_requires='>=3.6',
)