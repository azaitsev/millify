from distutils.core import setup
from millify import __version__, __author__

setup(
    name='millify',
    packages=['millify'],
    version=__version__,
    description='Convert long numbers into a human-readable format in Python',
    author=__author__,
    author_email='azaitsev@gmail.com',
    url='https://github.com/azaitsev/millify',
    keywords=['numbers', 'decimals', 'formatting', 'human-readable', 'pretty'],
    classifiers=[]
)
