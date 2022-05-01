import setuptools
# from .version import __version__
with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("mitesh/version.py", "r", encoding="utf-8") as fh:
    version = fh.read().split('=')[1].strip().replace("'", '')

setuptools.setup(
    name='mitesh',                                  # should match the package folder
    packages=['mitesh'],                            # should match the package folder
    version=version,                                # important for updates
    license='MIT',                                  # should match your chosen license
    description='Testing installation of Package',
    long_description='Modestly Integrated To Every SHell',  # loads your README.md
    long_description_content_type="text/x-rst",     # README.md is of type 'markdown'
    author='Mitesh Singh Jat',
    author_email="@".join(["mitesh.singh.jat", "gmail" + ".com"]),
    url='https://github.com/miteshbsjat/mitesh', 
    project_urls = {                                # Optional
        "Bug Tracker": "https://github.com/miteshbsjat/mitesh/issues"
    },
    install_requires=[],                            # list all packages that your package uses
    keywords=["pypi", "mitesh", "shell"],           #descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    
    download_url="https://github.com/miteshbsjat/mitesh/archive/refs/tags/0.0.0.tar.gz",
)