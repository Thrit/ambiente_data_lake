import setuptools

with open('README.md') as fp:
    long_description = fp.read()

setuptools.setup(
    name='ambiente_aws_data_lake',
    version='0.0.1',

    description='Criando meu primeiro data lake',
    long_description=long_description,
    long_description_content_type='text/markdown',

    author='author',

    package_dir={'': 'ambiente_aws_data_lake'},
    packages=setuptools.find_packages(where='ambiente_aws_data_lake'),

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed"
    ]
)