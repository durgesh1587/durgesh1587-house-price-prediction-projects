from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_objects:
        requirements = file_objects.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    return requirements

setup(
    name="HousePricePrediction",
    version="0.0.1",
    author="durgesh",
    author_email="durrgeshkharwar72@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages(),
)