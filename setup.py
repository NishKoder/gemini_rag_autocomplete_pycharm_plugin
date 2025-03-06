"""
Setup script for the gemini_rag_autocomplete package.
"""

from setuptools import setup, find_packages

# Read the contents of README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Package metadata
setup(
    name="gemini_rag_autocomplete",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A PyCharm plugin for code completion powered by Gemini and RAG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/gemini_rag_autocomplete",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "google-generativeai>=0.3.0",
        "numpy>=1.22.0",
        "requests>=2.27.0",
        "pyyaml>=6.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.1.0",
            "isort>=5.10.0",
            "mypy>=0.931",
            "flake8>=4.0.1",
        ],
    },
    entry_points={
        "console_scripts": [
            "gemini-rag=gemini_rag_autocomplete.main:main",
        ],
    },
)
