import setuptools

setuptools.setup(
        name="planets",
        version="0.0.1",
        packages=setuptools.find_namespace_packages(include=["planets.*"]),
        #packages=setuptools.find_packages(),
)
