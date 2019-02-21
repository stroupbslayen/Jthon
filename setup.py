from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pysonify',
    version='0.5.0',
    description='A JSON helper for Python',
    py_modules=['pysonify'],
    url='https://github.com/stroupbslayen/Pysonify',
    author='StroupBSlayen',
    author_email='',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6.0',
    classifiers=[
        'License :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: JSON',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
