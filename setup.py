from setuptools import setup
setup(name="FileFinder",
      version="1.0.0",
      description="Python script to find anything from your system.",
      long_description=open('README.md').read(), 
      long_description_content_type='text/markdown',
      author="Deepanshu antil",
      packages=['FileFinder'],
      author_email="deepanshuantil4113@gmail.com",
      url="https://github.com/deepanshu414",
      license="MIT", 
      install_requires=['psutil'])
