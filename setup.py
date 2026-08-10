from setuptools import setup,find_packages



setup(

name="ParsFramework",

version="1.0.0",

packages=find_packages(include=["ParsFramework","ParsFramework.*"]),
#packages=find_packages(),
#py_modules=["ParsFramework"],

description="Comprehensive tools for developers and users",

author="Pars Group",

author_email="info@parsframework.com",

url="https://parsframework.com",

python_requires=">=1.0",

)
