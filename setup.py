from setuptools import setup

setup(
    name = "sea_ice_drift",
    version = "0.7",
    author = 'Anton Korosov, Stefan Muckenhuber',
    author_email = "anton.korosov@nersc.no",
    description = ("Drift of sea ice from satellite data using feature tracking and pattern matching methods"),
    long_description = ("Drift of sea ice from satellite data using feature tracking and pattern matching methods"),
    license = "GNU General Public License v3",
    keywords = "sar, feature tracking, pattern matching, ice drift",
    url = "https://github.com/nansencenter/sea_ice_drift",
    download_url='https://github.com/nansencenter/sea_ice_drift/archive/v0.7.tar.gz',
    packages=['sea_ice_drift'],
    test_suite="sea_ice_drift.tests",
    install_requires=['nansat'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Utilities',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Intended Audience :: Science/Research',
    ],
)
