import os

from setuptools import setup, find_packages


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
    packages=find_packages(exclude=['tests', 'samples']),
    install_requires=['logstash-formatter'],
    url='',
    license='BSD',
    author='Surbhi Saraogi',
    author_email='surbhi.saraogi95@gmail.com',
    entry_points={
    },
    test_suite="tests",
    description='An easy to use logging library that provides a basic logging configuration which can be integrated '
                'with any python application.'
)