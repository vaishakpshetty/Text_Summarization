import setuptools

__version__ = "0.1.0"

REPO_NAME = "text_summarization"
USER_NAME = "vaishakpshetty"
SRC_REPO = "text_summarizer"
EMAIL = "vaishkshetty2000@gmail.com"

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=USER_NAME,
    author_email=EMAIL,
    description="Python package for text-summarization app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)



# or 
 
# HYPHEN_E_DOT ="-e ."
# from setuptools import find_packages, setup
# from typing import List

# def get_requirements(file_path:str)->List[str]:
#     """Functions returns the list of requirements"""
#     requirements = []
#     with open(file_path) as f:
#         requirements = f.readlines()
#         requirements = [req.replace("\n","")for req in requirements]

#         if HYPHEN_E_DOT in requirements:
#             requirements.remove(HYPHEN_E_DOT)

#     return requirements  


# setup(
#     name=SRC_REPO,
#     version=__version__,
#     author=USER_NAME,
#     author_email=EMAIL,
#     pacakages = find_packages(),
#     install_requires=get_requirements('requirements.txt')

# )