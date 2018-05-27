from setuptools import setup
from setuptools import find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='paybidelec',
      version='0.3.1',
      description='pay as a bid for electricity auction model',
      url='',
      author='Amirhosein Shirani',
      author_email='amirhhh.shirani@yahoo.com',
      license='Shatif University of Technology',
      packages=find_packages(),
      zip_safe=False)
