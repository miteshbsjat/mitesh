import setuptools
from setuptools.command.test import test as TestCommand
# from .version import __version__
with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()
exec(open('mitesh/version.py').read())


class Run_TestSuite(TestCommand):
    def run_tests(self):
        import os
        import sys

        py_version = sys.version_info[0]
        print('Python version from setup.py is', py_version)
        run_string = "python3 -m unittest tests/test_mitesh.py"
        os.system(run_string)


setuptools.setup(
    name='mitesh',                                  # should match the package folder
    packages=['mitesh'],                            # should match the package folder
    version=__version__,                            # important for updates
    license='Apache License 2.0',                   # should match your chosen license
    description='Modestly Integrated To Every SHell',
    long_description=long_description,              # loads your README.md
    long_description_content_type="text/x-rst",     # README.rst is of type 'x-rst'
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
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System',
        'Topic :: System :: Operating System',
        'Topic :: System :: Shells',
        'Topic :: System :: System Shells',
        'Topic :: System :: Systems Administration',
        'Topic :: Text Processing',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    
    download_url="https://github.com/miteshbsjat/mitesh/archive/refs/tags/0.0.0.tar.gz",
    cmdclass={'test': Run_TestSuite},
)