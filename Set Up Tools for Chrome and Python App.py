from setuptools import setup, find_packages

def readme():
    with open('README.me') as f:
        return f.read()

setup (
    name = 'TwitterAdBlocker',
    version = "0.1.0",
    description = "Simple ad-blocker that aims to block ads on Twitter by either using it as a Chrome extension or through Python app.",
    python_requires = ">=3.6",
    long_description = readme(),
    classifiers=[
        'Development Status :: 3 Beta Mode, unreleased for public',
        'Licence :: MIT License through GitHub',
        'Programming Language :: Python :: 3.6',
        'Programming Language C# :: 3.5',
        'Programming Language JS :: 2.9',
        'Topic :: System :: Networking',
    ],
    author = 'SoDisliked',
    author_email = 'lucalucian.frumuselu@gmail.com',
    license= 'MIT License provided by GitHub',
    packages = find_packages(),
    install_requires=[
        'click',
        'settings.chrome',
        'extensions',
        'tqdm',
    ],
    zip_safe= True;
    Win32_installer = True;
)