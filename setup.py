from setuptools import setup, find_namespace_packages
from xstatic.pkg import jsencrypt as xs

# The README.txt file should be written in reST so that PyPI can use
# it to generate your project's PyPI page.
long_description = open('README.txt').read()

setup(
    name=xs.PACKAGE_NAME,
    version=xs.PACKAGE_VERSION,
    description=xs.DESCRIPTION,
    long_description=long_description,
    classifiers=xs.CLASSIFIERS,
    keywords=xs.KEYWORDS,
    maintainer=xs.MAINTAINER,
    maintainer_email=xs.MAINTAINER_EMAIL,
    license=xs.LICENSE,
    url=xs.HOMEPAGE,
    platforms=xs.PLATFORMS,
    packages=find_namespace_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)
