import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jianshou-client",
    version="1.0.1",
    author="p1slave",
    author_email="p1slave@protonmail.com",
    description="Jianshou Client APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/p1slave/jianshou-client",
    project_urls={
        "Bug Tracker": "https://github.com/p1slave/jianshou-client/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3",
	install_requires=['requests', 'bs4', 'yattag', 'python-dotenv', 'pytest']
)