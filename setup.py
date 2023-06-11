import setuptools
from django_pyp8s import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-pyp8s",
    version=version,
    author="Pavel Kim",
    author_email="hello@pavelkim.com",
    description="Django application that provides an interface to pyp8s metrics collector",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pyp8s/django-pyp8s",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Framework :: Django :: 4",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pyp8s>=3.2.0",
        "Django>=4.0",
    ]
)
