import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="synthetic_datasets",
    version="0.1.10",
    description="synthetic datasets for benchmarking AI and machine learning",
    long_description=long_description,
    author="Dave MacDonald",
    author_email="dave@torontoai.org",

    packages=["synthetic_datasets"],
    include_package_data=True,

    # Details
    url="https://github.com/synthetic-datasets/synthetic-datasets",

    # Dependent packages (distributions)
    install_requires=[
        "numpy",
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )

)