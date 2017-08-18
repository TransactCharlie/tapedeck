from setuptools import setup, find_packages

setup(
    name="tapedeck",
    version="0.1",
    packages=find_packages("src"),
    package_dir={'': 'src'},
    install_requires=["Click"],
    entry_points='''
        [console_scripts]
        tapedeck=tapedeck.scripts.cli:tapedeck
        '''
)