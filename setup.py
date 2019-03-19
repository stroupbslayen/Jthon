from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='jthon',
    version='1.0.0',
    description='A JSON helper for Python',
    py_modules=['jthon'],
    url='https://github.com/stroupbslayen/Jthon',
    author='StroupBSlayen',
    author_email='',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6.0',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
