from setuptools import setup


setup (
    name="formatSlackMessage",
    version="1.0.0",
    description="A project to format the slack messages in a structured way",
    author="Bilal Peerzade",
    author_email="bilalpeerzade@gmail.com",
    packages=['formatslackmessage'],
    package_dir={"":"src"},
    install_requires=[
        "pandas >= 1.5.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Development Status :: 5 - Production/Stable"
    ]
)
