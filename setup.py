import setuptools

VERSION = '0.5.2'

packages = [
    'vk_air',
    'vk_air.objects'
]

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setuptools.setup(
    name='vk_air',
    author='sultan1k',
    description='Фреймворк на Python для VK API',
    version=VERSION,
    packages=packages,
    url='https://github.com/sultan1k/vk_air',
    include_package_data=True,
    python_requires='>=3.8.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)