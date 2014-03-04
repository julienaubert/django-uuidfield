from setuptools import setup, find_packages

setup(
    name='django-uuidfield',
    version='0.5.0',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    description='UUIDField in Django',
    url='https://github.com/dcramer/django-uuidfield',
    zip_safe=False,
    install_requires=[
        'django', 'six'
    ],
    tests_require=[
        'psycopg2', 'coverage'
    ],
    packages=find_packages(),
    test_suite='runtests.runtests',
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
    ],
)
