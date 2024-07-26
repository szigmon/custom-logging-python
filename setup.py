from setuptools import setup, find_packages

setup(
    name='custom_logging',
    version='1.0.0',
    description='A robust Python logging library leveraging the default logging library to provide enhanced logging capabilities with custom JSON formatting and enrichment.',
    author='Sagi Zigmon',
    author_email='szigmon@redhat.com',
    url='https://github.com/szigmon/custom-logger-python',
    url='https://github.com/szigmon/custom-logging-python',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
