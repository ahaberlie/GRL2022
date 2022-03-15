from setuptools import setup, find_namespace_packages

setup(name='grl2022',
      version='0.1',
      description='Future Thunderstorm Changes Supporting Code',
      author='Alex Haberlie',
      author_email='ahaberlie1@niu.edu',
      package_dir={'':'src'},
      packages=find_namespace_packages(where="src"),
      url='https://ahaberlie.github.io/'
     )