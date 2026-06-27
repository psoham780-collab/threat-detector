from setuptools import setup, find_packages

setup(
    name="cybershield-ai",
    version="0.1.0",
    description="Threat detector web app",
    packages=find_packages(where="app", exclude=["dataset", "static", "templates"]),
    package_dir={"": "app"},
)
