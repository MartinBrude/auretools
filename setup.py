import setuptools

with open("DESCRIPTION.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='auretools',
    version='1.1.0',
    author='Ferchus',
    author_email='fer@chus.ai',
    description='A compilation of F utility functions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/MartinBrude/auretools',
    project_urls = {
        "Bug Tracker": "https://github.com/institutohumai/humai_utils/issues"
    },
    license='MIT',
    packages=['auretools'],
    install_requires=['requests'],
)