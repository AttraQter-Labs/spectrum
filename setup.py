from setuptools import setup, find_packages

setup(
    name="spectrum",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        "test": ["pytest>=7.0.0"],
    },
    python_requires=">=3.12",
)
