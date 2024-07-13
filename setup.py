from setuptools import find_packages,setup
from typing import List
def get_req(file:str)->List[str]:
    req=[]
    with open(file) as file_obj:
        req=file_obj.readline()
        req=[r.replace("\n","") for r in req ]
    return req
    
setup(
name="mlproject",
version="0.0.1",
author_email="sk.intellicy@gmail.com",
packages=find_packages(),
install_requires=get_req("requirements.txt")

)