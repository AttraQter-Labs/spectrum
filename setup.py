"""
Spectrum - Deterministic Measurement Infrastructure
"""

from setuptools import setup, find_packages

setup(
    name="spectrum",
    version="1.0.0+deterministic",
    description="Commercial-grade deterministic measurement and audit engines",
    author="AttraQtor-Labs LLC",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        # No external dependencies - deterministic by design
    ],
    extras_require={
        "dev": [
            "pytest>=9.0.0",
        ],
    },
)
