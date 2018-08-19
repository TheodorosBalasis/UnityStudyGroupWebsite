import setuptools

setuptools.setup(
    name='usgw',
    version="0",
    url='unitystudygroup.com',
    maintainer='unitystudygroup',
    maintainer_email='',
    packages=[
        'usgw',
        'usgw.bin',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'pymongo'
    ],
    entry_points={'console_scripts':[
        'usgw-config=usgw.bin.config:main',
    ]},
)
