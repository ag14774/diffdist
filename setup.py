from distutils.core import setup
setup(
  name = 'diffdist',
  packages = ['diffdist'],
  version = '0.1',
  license='GNU GPLv3',
  description = 'Provides differentiable communication primitives such as Send/Recv/Gather etc for pytorch. Autograd can backpropagate through those, making distributed model parallel models easy to implement.',
  author = 'Andreas Georgiou',
  author_email = 'geandrea@ethz.ch',
  url = 'https://github.com/ag14774/diffdist',
  download_url = 'https://github.com/ag14774/diffdist/archive/v0.1.tar.gz',
  keywords = ['torch', 'distributed', 'autograd', 'model', 'parallel', 'differentiable', 'backpropagate'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)
