from setuptools import setup, find_packages

setup(
    name="tiny-vm-desktop",
    version="0.1",
    description="A Desktop Environment for Tiny Virtual Machines",
    author="Your Name",
    author_email="youremail@example.com",
    packages=find_packages(),
    install_requires=[
        "qemu",
        "tkinter",
        "psutil",
        "pytest",
        "requests"
    ],
    entry_points={
        'console_scripts': [
            'tiny-vm-desktop=src.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
