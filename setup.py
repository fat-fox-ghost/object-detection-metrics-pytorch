from setuptools import setup, find_packages

setup_info = dict(
    name='object_detection_metrics_pytorch',
    version='0.0.1',
    author='fat-fox-ghost',
    author_email='',
    url='https://github.com/fat-fox-ghost/object-detection-metrics-pytorch',
    project_urls={
        'Bug Tracker': 'https://github.com/fat-fox-ghost/object-detection-'
                       'metrics-pytorch/issues'
    },
    description='Small library for working with results of object detection'
                'models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Topic :: Topic :: Scientific/Engineering :: Visualization',
    ],

    # Packages
    packages=['object_detection_metrics_pytorch'],
    package_dir={'object_detection_metrics_pytorch': 'src'},

    # CSV data
    # include_package_data=True,

    # Dependencies
    install_requires=open('requirements.txt').read().split('\n'),
    python_requires='>=3.6',
)

setup(**setup_info)
