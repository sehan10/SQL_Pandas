from distutils.core import setup
from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
  name = 'sqlDataframe',         # How you named your package folder (MyLib)
  packages = ['sqlDataframe'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This is an idea to further simplify the process of fetching/storing data into structured databases using pandas',   # Give a short description about your library
  author = 'Arsal Rahim | Sehan Ahmed Farooqui',                   # Type in your name
  author_email = 'arsalrahim1994@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/sehan10/SQL_Pandas.git',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/sehan10/SQL_Pandas/archive/0.1.tar.gz',    # I explain this later on
  keywords = ['Pandas', 'Dataframe', 'Structured databases', 'SQL query'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'Pandas',
          'SQLAlchemy',
	  'pyodbc'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
long_description_content_type='text/markdown',
long_description=long_description,

)
