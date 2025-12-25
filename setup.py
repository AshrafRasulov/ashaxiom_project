from setuptools import setup, find_packages

setup(
    name="ashaxiom",
    version="2.2.0",
    author="Ashraf",
    description="Intelligent Math & Financial Framework with Interactive Academy",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True, # Важно для HTML
    package_data={
        'ashaxiom': ['ashaxiom-lesson/**/*'], # Включаем все файлы документации
    },
    install_requires=[
        "numpy", "sympy", "matplotlib", "pandas", "scipy", "yfinance", "statsmodels", "openpyxl"
    ],
    classifiers=[
        "Framework :: Jupyter",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)