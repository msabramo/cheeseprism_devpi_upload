from setuptools import find_packages
from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='cheeseprism_devpi_upload',
    version='0.0.0',
    description='Make CheesePrism upload to devpi',
    long_description=README,
    author='Marc Abramowitz',
    author_email='marca-at-surveymonkey-dot-com',
    url='https://github.com/SMFOSS/cheeseprism_devpi_upload',
    keywords='cheeseprism pyramid devpi',
    py_modules=['cheeseprism_devpi_upload'],
    zip_safe=False,
    install_requires=['devpi-client'],
    entry_points = """\
    [cheeseprism.on_upload]
    devpi_upload = cheeseprism_devpi_upload:upload
    """,
)
