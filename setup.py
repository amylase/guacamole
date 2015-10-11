from distutils.core import setup

setup(name='guacamole',
      version='1.0',
      packages=['mirt'],
      py_modules=['start_mirt_pipeline'],
      install_requires=['numpy', 'scipy', 'affinity', 'matplotlib'])


