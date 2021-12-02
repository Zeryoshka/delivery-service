import os
from importlib.machinery import SourceFileLoader

from pkg_resources import parse_requirements
from setuptools import find_packages, setup


module = SourceFileLoader(
    'delivery-service', os.path.join('app', '__init__.py')
).load_module()

def load_requirements(fname: str) -> list:
    requirements = []
    with open(fname, 'r') as f:
        for req in parse_requirements(f.read()):
            extras = f'[{",".join(req.extras)}]' if req.extras else ''
            requirements.append(f'{req.name}{extras}{req.specifier}')
    return requirements

setup(
    name='delivery-service',
    version=module.__version__,
    description=module.__doc__,
    url='https://github.com/Zeryoshka/delivery-service',
    platforms='all',
    python_requires='>=3.9',
    packages=find_packages(exclude=['tests']),
    install_requires=load_requirements('requirements.txt'),
    extras_require={
        'dev': load_requirements('requirements.dev.txt')
    },
    entry_points={
        'console_scripts': [
            'delivery-api=app.__main__:main'
        ]
    },
    include_package_data=True
)
