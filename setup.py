'''
Function:
    setup the noveldl
Author:
    Charles
微信公众号:
    Charles的皮卡丘
GitHub:
    https://github.com/CharlesPikachu
'''
import noveldl
from setuptools import setup, find_packages


'''readme'''
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


'''setup'''
setup(
    name=noveldl.__title__,
    version=noveldl.__version__,
    description=noveldl.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    author=noveldl.__author__,
    url=noveldl.__url__,
    author_email=noveldl.__email__,
    license=noveldl.__license__,
    include_package_data=True,
    entry_points={'console_scripts': ['noveldl = noveldl.noveldl:noveldlcmd']},
    install_requires=list(open('requirements.txt', 'r').readlines()),
    zip_safe=True,
    packages=find_packages()
)