from distutils.core import setup

setup(
    name="synthetic_datasets",
    version="0.1.0",
    description="synthetic datasets for benchmarking AI and machine learning",

    author="Dave MacDonald",
    author_email="dave@torontoai.org",

    license="MIT",
    packages=["synthetic_datasets"],
    include_package_data=True,

    # Details
    url="https://github.com/synthetic-datasets/synthetic-datasets",

    # Dependent packages (distributions)
    install_requires=[
        "numpy",
    ]
)