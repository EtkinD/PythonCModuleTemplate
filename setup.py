from setuptools import setup, Extension, find_packages

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
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.8",
    ext_modules=[module],
    package_data={
        # Required for .pyi files to be included in the package
        "pycmtemplate": ["py.typed"],
    },
    entry_points={
        # Provide a console script entry point. After pip install run `pycmtemplate` on the command line
        "console_scripts": [
            "pycmtemplate = pycmtemplate.__main__:main",
        ],
    },
)
