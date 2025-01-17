from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='locustgraphqlclient',
    version='0.0.2',
    packages=['locustgraphqlclient'],
    url='https://github.com/rahulnoobest/locustgraphqlclient',
    license='Apache License 2.0',
    author='rahulnoobest',
    author_email='',
    description='Locust GraphQL client GraphQL. This is a GraphQLLocust equivalent of HttpLocust',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'graphqlclient@git+https://github.com/alaptseu/python-graphql-client.git@master',
        'locust'
    ]
)
