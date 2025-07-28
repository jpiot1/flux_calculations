[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"                # your package name on PyPI
version = "0.1.0"                  # current version
description = "Short description of what your package does."
readme = "README.md"
requires-python = ">=3.8"
authors = [
    { name="Your Name", email="youremail@example.com" }
]
license = { text = "MIT" }

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

# Optional dependencies for your package
dependencies = [
    "numpy >= 1.25",
    "pandas >= 2.0"
]

[tool.setuptools.packages.find]
where = ["src"]