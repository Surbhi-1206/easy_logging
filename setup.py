import os

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_version():
    basedir = os.path.dirname(__file__)
    try:
        with open(os.path.join(basedir, 'logging_config/version.py')) as f:
            locals = {}
            exec(f.read(), locals)
            return locals['VERSION']
    except Exception as e:
        raise RuntimeError('No version info found.')


setup(
    name='easy_logging',
    version=get_version(),
    description='An easy to use logging library',
    long_description=long_description,
    author='Surbhi Saraogi',
    author_email='surbhi.saraogi95@gmail.com',
    long_description_content_type="text/markdown",
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=['tests', 'samples']),
    install_requires=['logstash-formatter'],
    url='https://github.com/Surbhi-1206/easy_logging',
    entry_points={
    },
)
