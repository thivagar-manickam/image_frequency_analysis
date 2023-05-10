from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="image_frequency_analysis",
    version="0.2.2",
    author="M Thivagar",
    packages=find_packages(),
    install_requires=["opencv-python", "numpy", "pandas", "matplotlib"],
    python_requires=">=3.6",
    description="A package to perform image frequency analysis using the Fourier Transform method",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thivagar-manickam/image_frequency_analysis",
    project_urls={
        "Source": "https://github.com/thivagar-manickam/image_frequency_analysis",
        "Issues": "https://github.com/thivagar-manickam/image_frequency_analysis/issues",
        "Pull Requests": "https://github.com/thivagar-manickam/image_frequency_analysis/pulls",
    },
    license="MIT",
)
