from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    this fuction will return list of requirements
    """
    requirement_list:List[str] = [
        'pymongo==4.2.0',
        
        ]
    return requirement_list

__version__ = '0.0.1'

with open("README.md", "r", encoding="utf-8") as f:
    long_description=f.read()

REPO_NAME="Sensor-Fault-Detection"
AUTHOR_NAME="dipdregan"
SRC_REPO="Sensor_Fault_Detection"
AUTHOR_Email="dipendrapratap155@gmail.com"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_Email,
    description="this is sensor fault prediction project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    
    project_urls={
                  
    "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",  
                  
                 },
    package_dir={"":"Sensor_Fault_Detection"},
    packages=find_packages(where="Sensor_Fault_Detection"),
    install_requires = get_requirements()
)


