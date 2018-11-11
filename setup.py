from setuptools import setup

setup(
    name='cilimao-cli',
    version = '1.0',
    license="MIT",
    py_modules=['cilimao'],
    install_requires=['requests', 'docopt'],

    author = 'imorta',
    author_email = 'evanxian9@gmail.com',


    entry_points={
        'console_scripts': ['cilimao-cli=cilimao:run']
    },
)