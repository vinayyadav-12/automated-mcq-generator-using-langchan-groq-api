from setuptools import setup, find_packages

setup(
    name="mcqgenerator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "huggingface-hub",
        "langchain",
        "streamlit",
        "python-dotenv",
        "pypdf2",
        "langchain-community",
        "langchain-huggingface",
        "pandas"
    ]
)