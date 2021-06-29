import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="magic_config",
    version="0.1.0",
    author="mogaiskii",
    author_email="sani.mog@gmail.com",
    description="declarative settings with multiple backends",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mogaiskii/magic_config",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    license="MIT",
    keywords=["config", "settings", "configuration"],
    install_requires=[
        'pyyaml~=5.4.1',
    ]
)

