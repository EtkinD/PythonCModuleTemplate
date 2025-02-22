from setuptools import setup, Extension

# C/C++ extension module configuration
module = Extension(
    "pycmtemplate_c",
    sources=["src/main.cpp"],
    include_dirs=[],
    extra_compile_args=["-std=c++11"],
)

setup(
    name="pycmtemplate",
    version="0.0.1",
    description="Python C template",
    long_description="Python C/C++ template project",
    author="Etkin Dogan",
    author_email="etkindogan@gmail.com",
    python_requires=">=3.8",
    ext_modules=[module],
)
