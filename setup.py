import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="extract_specific_lines",
    version="0.0.3",
    author='Guanliang Meng',
    author_email='linzhi2012@gmail.com',
    description="to get specific lines from the subject file which maps the query ids. Written by Guanliang MENG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3',
    url='https://github.com/linzhi2013/extract_specific_lines',
    packages=setuptools.find_packages(),
    include_package_data=True,
    # install_requires=[''],

    entry_points={
        'console_scripts': [
            'extract_specific_lines=extract_specific_lines.extract_specific_lines:main',
        ],
    },
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ),
)