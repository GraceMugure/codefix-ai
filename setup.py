from setuptools import setup, find_packages

setup(
    name="codefix-ai",
    version="0.1.0",
    description="CodeFix AI: Run Python code and get error explanations in plain English",
    author="Grace Mugure",
    author_email="ndungugracie06@gmail.com",
    url="https://github.com/GraceMugure/codefix-ai",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "codefix-ai = codefix_ai.codefix_ai:main"
        ]
    },
    install_requires=[
        "requests",
    ],
    long_description_content_type="text/markdown",
    long_description=open("README.md", encoding="utf-8").read(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
