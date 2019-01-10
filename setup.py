from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='modelarchive',
    version='0.0.1',
    author='Barak Nehoran',
    author_email='bnehoran@users.noreply.github.com',
    description='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    scripts=[],
    url="https://github.com/seung-lab/modelarchive",
    setup_requires=[
        'pbr',
    ],
    pbr=True,
)
