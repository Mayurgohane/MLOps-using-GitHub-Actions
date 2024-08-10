import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "mayur"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "mayurgohane19@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=Mayurgohane,
    author_email=mayurgohane19@gmail.com,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{Mayurgohane}/{Text-Classification-with-MLOps-using-GitHub-Actions}",
    project_urls={
        "Bug Tracker": f"https://github.com/{Mayurgohane}/{Text-Classification-with-MLOps-using-GitHub-Actions}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)