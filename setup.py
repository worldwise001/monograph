from setuptools import setup, find_packages

from monograph import VERSION

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name="monograph",
    version=VERSION,
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,

    # metadata to display on PyPI
    author="Sarah Harvey",
    author_email="s@shh.sh",
    description="visualizer of research papers",
    keywords="monograph research paper",
    url="https://github.com/worldwise001/monograph",
)
