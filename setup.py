from setuptools import find_packages, setup

setup(
    name="Flask-SaaSify",
    version="0.0.5",
    author="Koen van Eijk",
    author_email="vaneijk.koen@gmail.com",
    description="A Flask toolbox for rapidly building SaaS applications.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/koenvaneijk/flask-saasify",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask>=2.0",
        "Flask-Login",
        "Flask-SQLAlchemy",
        "Flask-Migrate",
        "Flask-WTF",
        "email-validator",
        "python-dotenv",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)
