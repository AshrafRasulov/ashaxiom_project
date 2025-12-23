from setuptools import setup, find_packages

setup(
    name="ashaxiom",
    version="1.2.0", # Твоя текущая стабильная версия
    author="Ashraf Rasulov",
    author_email="your_email@example.com",
    description="Intelligent Analytical Framework for Higher Mathematics",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AshrafRasulov/ashaxiom_project",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "sympy",
        "matplotlib",
        "scipy",
        "pandas",
        "openpyxl"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Jupyter",
    ],
    python_requires='>=3.7',
)