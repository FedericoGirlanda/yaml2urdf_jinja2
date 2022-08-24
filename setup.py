from setuptools import setup, find_packages

setup(
    name='yaml2urdf_jinja2',
    author='Federico Girlanda',
    version='1.0.0',
    url="https://github.com/FedericoGirlanda/yaml2urdf_jinja2",
    packages=find_packages(),
    install_requires=[
        'Jinja2'
    ],
    classifiers=[
          'Development Status :: 5 - Stable',
          'Environment :: Console',
          'Intended Audience :: Academic Usage',
          'Programming Language :: Python',
          ],
)