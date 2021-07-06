from setuptools import setup,find_packages

setup(name="imageai",
      version='2.1.5-custom',
      description='A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities',
      url="https://github.com/aaros-pl/ImageAI",
      author='Moses Olafenwa and John Olafenwa',
      author_email='guymodscientist@gmail.com',
      license='MIT',
      packages= find_packages(),
      install_requires=['tensorflow-gpu==1.14.0','numpy','scipy','pillow','matplotlib', 'h5py==2.10.0', 'keras==2.3.1'],
      zip_safe=False

      )