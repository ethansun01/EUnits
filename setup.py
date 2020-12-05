import setuptools

with open("README.org", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EUnits",
    version="0.0.2",
    author="Ethan Sunshine",
    author_email="author@example.com",
    description="A simple units package",
    long_description='This python package adds a single class, the Quantity. It is meant to help you keep track of units when doing physical/scientific/engineering calculations.',
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

print('setup.py running!')
