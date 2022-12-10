import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="postgres-database-utils",
    version="0.1.0",
    author="apinanyogaratnam",
    author_email="apinanapinan@icloud.com",
    description="A package for postgres database utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apinanyogaratnam/database-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10.4",
    install_requires=[
        "psycopg2-binary",
        "pandas",
    ],
)
