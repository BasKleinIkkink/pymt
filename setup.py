from setuptools import setup

setup(
    name="pymt",
    version="0.0.6",
    author="Nynra",
    description="A module for Merkle Tries and proofs.",
    py_modules=["pymt"],
    package_dir={"": "src"},
    install_requires=["cytoolz", "eth-hash", "eth-typing", 
                      "eth-utils", "pycryptodome", "rlp", "toolz"],
)