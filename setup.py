"""
The setup.py file is an essential part of packaging 
and distributing python project. It is used by setuptools
to define the configuration of your project, such as its metadata, dependencies """

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and editable install flag
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Pourush Kumar Gupta",
    author_email="pourushgupta59@gmai.com",
    packages=find_packages(),  # corrected here
    install_requires=get_requirements()
)
