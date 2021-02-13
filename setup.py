from setuptools import setup

setup(
   name='tspam',
   version='0.1',
   description='A very simple sms-spammer',
   author='AndreyBorisov',
   author_email='andrey.borisov@outlook.de',
   packages=['tspam'],  #same as name
   package_dir={'tspam': 'src/tspam'},
   package_data={'tspam': ['data/*.json']},
   include_package_data=True,
   entry_points={'console_scripts': [ 'tspam=tspam.start:MAIN']},
       # function to call on $ python my.egg
    py_modules=['tspam.start:MAIN'],
    license="MPL 2.0",
   install_requires=['asyncio', 'aiohttp', "requests", "colorama","urllib3"], #external packages as dependencies
)
