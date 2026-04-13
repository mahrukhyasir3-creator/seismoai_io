from setuptools import setup

setup(
    name="seismoai_io",
    version="0.1",
    py_modules=["seismoai_io"],
    install_requires=[
        "numpy",
        "segyio"
    ]
)
