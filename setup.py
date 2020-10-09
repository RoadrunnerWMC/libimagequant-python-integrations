import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='libimagequant_integrations',
    version='1.1.0',
    author='RoadrunnerWMC',
    author_email='roadrunnerwmc@gmail.com',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/RoadrunnerWMC/libimagequant-python-integrations',
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
    install_requires=[
        'libimagequant',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Multimedia :: Graphics',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ],
)