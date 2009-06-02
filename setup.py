from setuptools import setup, find_packages
import os

version = open(os.path.join("sc", "pfg", "brazilianfields", "version.txt")).read().strip()

setup(name='sc.pfg.brazilianfields',
      version=version,
      description="Brazilian fields and widgets to be used with PloneFormGen",
      long_description=open(os.path.join("sc", "pfg", "brazilianfields", "README.txt")).read().decode('UTF8').encode('ASCII', 'replace') + '\n' +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone archetypes FormGen BrFieldsAndWidgets brazil brasil pfg',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      url='http://plone.org/products/sc.pfg.brazilianfields',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sc','sc.pfg'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.BrFieldsAndWidgets',
          'Products.PloneFormGen'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
