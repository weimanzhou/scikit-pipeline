import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scikit-pipeline",
    version="0.0.1",
    author="snowflake",
    author_email="weimanzhou1206@gmail.com",
    description="scikit-pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/weimanzhou/scikit-pipeline",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
