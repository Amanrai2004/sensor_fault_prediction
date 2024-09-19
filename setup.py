from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e.'



def get_req(file_path :str)->list[str]:
    requirements = []
    with open (file_path)as file_obj:
        requirements=  file_obj.readlines()
        requirements= [req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements


setup(
    name = "fault dection",
    version="0.0.1",
    author="aman rai",
    author_email='amnrai2004@gmail.com',
    install_requirements =  get_req('requirements.txt'),
    packages=find_packages(),
)