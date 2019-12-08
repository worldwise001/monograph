from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name="monograph",
    version="0.1",
    packages=find_packages(),
    install_requires=install_requires,

    # metadata to display on PyPI
    author="Sarah Harvey",
    author_email="s@shh.sh",
    description="visualizer of research papers",
    keywords="monograph research paper",
    url="https://github.com/worldwise001/monograph",
)
