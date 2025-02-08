# setup.py
from setuptools import setup, find_packages

setup(
    name="ArabicTextCleaner",
    version="0.1.0",
    description="A Python library for cleaning Arabic text for NLP applications.",
    author="Mody Medhat",
    author_email="moody.medhat99@gmail.com",
    url="https://github.com/yourusername/arabic_text_cleaner",
    packages=find_packages(),
    install_requires=[
        # No external dependencies are needed for this minimal version.
    ],
    classifiers=[
        "Programming Language :: Python :: 3.13.1",
        "License :: OSI Approved :: MIT License",
    ],
)
