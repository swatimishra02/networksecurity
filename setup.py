# setup.py is used by setuptools to define the configuration of a project such as metadata, dependencies and more.

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str] :
    # this function returns a list of requirements

    requirement_list:List[str] = []

    try :
        with open('requirements.txt', 'r') as file :
            # read lines from the file
            lines = file.readlines()
            # process each line
            for line in lines:
                requirement = line.strip()
                #cignore empty lines and -e .
                if requirement and requirement != '-e .' :
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found!")

    return requirement_list

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Swati Mishra",
    author_email = "swatimishra0209@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)