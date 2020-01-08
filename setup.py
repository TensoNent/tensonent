"""
setup.py is the build script for setuptools. It tells setuptools about your
package (such as the name and version) as well as which code files to include.
"""

import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="tensonent",
    version="0.1.3",
    author="Milad Sadeghi.DM",
    author_email="EverLookNeverSee@ProtonMail.ch",
    description="Tensor Decomposition Library",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/Tensopy/tensopy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
