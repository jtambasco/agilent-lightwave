from setuptools import setup

setup(name='agilent-lightwave',
      version='0.2',
      description='Python driver for the Agilent Lightwave 8164A/B.',
      url='https://github.com/jtambasco/agilent-lightwave',
      author='Jean-Luc Tambasco',
      author_email='an.obscurity@gmail.com',
      license='MIT',
      install_requires=[
          'tqdm',
          'scipy',
          'numpy'
      ],
      packages=['agilent-lightwave'],
      include_package_data=True,
      zip_safe=False)
