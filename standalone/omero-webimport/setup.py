from setuptools import setup, find_packages

setup(
    name='omero-webimport',
    version='0.0.1dev',
    description="OMERO.web plugin to import images to OMERO",
    # long_description=long_description,
    author="Nottingham SEGP Group 12",
    author_email="vernonlim2004@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU Affero General Public License v3 ",  # noqa
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],  # Get strings from
    packages=find_packages(exclude=['ez_setup']),
    install_requires=['omero-web>=5.6.0'],
    keywords=['OMERO.web', 'import'],
)
