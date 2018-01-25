from setuptools import setup, find_packages


requires = open("requirements.txt").read().split("\n")

setup(
    name="fxdayu_dataz",
    version="0.0.1",
    packages=find_packages(),
    install_requires=requires,
    entry_points={"console_scripts": ["dataz = fxdayu_dataz.dataz:dataz",
                                      "rqadjust = fxdayu_dataz.adjust.rqadjust:rqadjust"]}
)
