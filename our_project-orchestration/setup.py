from setuptools import find_packages, setup

setup(
    name="our_project_orchestration",
    packages=find_packages(exclude=["our_project_orchestration_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
