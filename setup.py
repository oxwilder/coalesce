from setuptools import setup, find_packages


setup(
    name='coalesce',
    version='0.1',
    license='',
    author="John Patterson",
    author_email='john@jpatterson.io',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/oxwilder/coalesce',
    keywords='null coalescing operator',
)
