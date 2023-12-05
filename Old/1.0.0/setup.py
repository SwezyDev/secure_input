from setuptools import setup, find_packages


VERSION = '1.0.0'
DESCRIPTION = 'Secure Password Input'
LONG_DESCRIPTION = 'A package that allows to write a password or key in a Secure way'

setup(
    name="secure_input",
    version=VERSION,
    author="Swezy (https://discord.gg/KkxjCe8Fg2)",
    author_email="swezysoftware@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=['secure_input'],
    install_requires=[],
    keywords=['python', 'secure', 'password', 'input', 'key', 'encryption'],
    classifiers=[
        "Development Status :: 1 - Release",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
