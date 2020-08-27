from setuptools import setup
from pandas import Categorical, get_dummies

setup(
      name='my_custom_sklearn_transforms',
      version='1.0',
      description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      ''',
      url='https://github.com/igorvroberto/Maratona-IBM-2020/desafio-04/sklearn_transforms',
      author='Igor Roberto',
      author_email='igorvroberto@gmail.com',
      license='BSD',
      packages=[
            'my_custom_sklearn_transforms'
      ],
      zip_safe=False
)
