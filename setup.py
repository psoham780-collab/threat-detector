from setuptools import find_packages, setup

setup(
    name="cybershield-ai",
    version="0.1.0",
    description="Threat detector web app",
    packages=find_packages(
        include=["app", "app.*"],
        exclude=["tests", "dataset", "static", "templates"],
    ),
)
