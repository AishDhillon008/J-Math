from setuptools import setup

setup(
    # The name people will type: pip install jmath-framework
    # (Just 'jmath' might be taken by someone else, so this is safer and sounds professional)
    name='jmath-framework', 
    
    # Your first official version!
    version='0.1.0',
    
    # A short description of your math
    description='A non-Archimedean mathematical framework for evaluating limits and infinities algebraically.',
    
    # Your GitHub username
    author='AishDhillon008',
    
    # The link to your GitHub repository
    url='https://github.com/AishDhillon008/J-Math',
    
    # This tells PyPI to specifically look for your jmath.py file
    py_modules=['jmath'], 
    
    # Standard tags that make your project look professional on the PyPI website
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics'
    ],
)

