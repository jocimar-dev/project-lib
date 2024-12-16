from setuptools import setup, find_packages

setup(
    name="jocimar-dev-project-test-lib-ciandt",
    version="0.1.1",
    description="Uma biblioteca de exemplo para GitHub Packages",
    url="https://github.com/jocimar-dev/project-lib",
    author="Jocimar",
    author_email="jocimarneres@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
