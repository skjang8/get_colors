from setuptools import setup

setup(
    name="get_colors",
    version="0.2.0",
    author="skjang8",
    author_email="skjang8@gmail.com",
    description="A simple utility to generate colors from various colormaps",
    long_description=open("README.md").read() if hasattr(__builtins__, "open") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/skjang8/get_colors",
    py_modules=["get_colors"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
    ],
) 
