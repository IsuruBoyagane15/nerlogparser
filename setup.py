from setuptools import setup

setup(name='nerlogparser',
      version='0.0.1',
      description='Automatic log parser',
      long_description='Automatic log parser using named entity recognition in Python',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
      ],
      keywords='named entity recognition, log parser, log forensics',
      url='http://github.com/studiawan/nerlogparser/',
      author='Guillaume Genthial, Hudan Studiawan',
      author_email='studiawan@gmail.com',
      license='Apache',
      packages=['nerlogparser'],
      install_requires=[
	'tensorflow',
	'logging'
      ],
      include_package_data=True,
      zip_safe=False)
