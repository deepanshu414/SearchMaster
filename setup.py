from setuptools import setup
setup(name="SearchMaster",
      version="1.1.1",
      description="Python script to find anything from your system.",
      long_description=open('README.md').read(), 
      long_description_content_type='text/markdown',
      author="Deepanshu antil",
      packages=['SearchMaster'],
      author_email="deepanshuantil4113@gmail.com",
      url="https://github.com/deepanshu414",
      license="MIT", 
      install_requires=['psutil'])
