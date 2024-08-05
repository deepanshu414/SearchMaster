from setuptools import setup
setup(name="SearchMaster",
      version="1.1.1",
      description="SearchMaster is a Python library that helps you search for files with a specified name across all available drives on your system.",
      long_description=open('README.md').read(), 
      long_description_content_type='text/markdown',
      author="Deepanshu antil",
      maintainer="Deepanshu antil",
      packages=['SearchMaster'],
      author_email="deepanshuantil4113@gmail.com",
      url="https://github.com/deepanshu414/find_allx",
      license="MIT", 
      install_requires=['psutil'])
