from setuptools import setup
from io import open


def readme():
    with open('README.rst', encoding='utf-8') as f:
        return '\n' + f.read()


MAJOR               = 0
MINOR               = 0
MICRO               = 0
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)


setup(name='russellcapping',
      version=VERSION,
      description='Single level FTSE Russell Capping Methodology implementation',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Financial and Insurance Industry',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Office/Business :: Financial',
          'Topic :: Software Development :: Build Tools',
      ],
      keywords=[
          'api',
          'financial',
      ],
      url='https://github.com/saporitigianni/russellcapping',
      download_url='https://pypi.python.org/pypi/russellcapping',
      author='Gianni Saporiti',
      author_email='saporitigianni@outlook.com',
      python_requires='>=3',
      license='BSD 3-Clause License',
      packages=['russellcapping'],
      install_requires=[
      ],
      include_package_data=True,
      zip_safe=False)
