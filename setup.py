from setuptools import setup

setup(name='agilentlightwave',
      version='0.2',
      description='Python driver for the Agilent Lightwave 8164A/B.',
      url='https://github.com/jtambasco/agilentlightwave',
      author='Jean-Luc Tambasco',
      author_email='an.obscurity@gmail.com',
      license='MIT',
      install_requires=[
          'tqdm',
          'scipy',
          'numpy'
      ],
      packages=['agilentlightwave'],
      include_package_data=True,
      zip_safe=False)
