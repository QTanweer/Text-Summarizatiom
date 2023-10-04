import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


__version__ = '0.0.0'

REPO_NAME = 'Text-Summarization'
AUTHOR_NAME = 'QTanweer'
SRC_REPO = 'textSummarization'
SRC_PATH = 'src'
AUTHOR_EMAIL = 'qtanweer.mts41ceme@gmail.com'
 

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QTanweer/Text-Summarization.git",
    package_dir={'': SRC_PATH},
    packages=setuptools.find_packages(where=SRC_PATH)
)