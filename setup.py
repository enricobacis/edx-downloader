from distutils.core import setup
import shutil
import os

# rename script
if not os.path.exists('build/scripts'):
    os.makedirs('build/scripts')
shutil.copyfile('edx-dl.py', 'build/scripts/edx-downloader')

setup(
    name='edx-downloader',
    version='0.1',
    url='https://github.com/shk3/edx-downloader',
    description='A simple tool to download video lectures from edx.org.',
    long_description=open('README.md').read(),
    author='shk3',
    author_email='shk3@users.noreply.github.com',
    maintainer='enricobacis',
    maintainer_email='enrico.bacis@gmail.com',
    requires=['youtube_dl', 'beautifulsoup4'],
    scripts=['build/scripts/edx-downloader'],
)
