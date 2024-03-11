import os

from setuptools import setup, find_packages


def _get_version():
    version_file = os.path.normpath(
        os.path.join(os.path.dirname(__file__), "stock_info", "VERSION")
    )
    with open(version_file) as fh:
        version = fh.read().strip()
        return version


setup(
    name="stock_info",
    version="0.1.0",
    description="A Python package for fetching and processing stock information.",
    author="qrtt1",
    author_email="chingyichan.tw@gmail.com",
    packages=find_packages(),
    install_requires=[
        # 列出這個套件需要依賴的其他套件
        # 例如: 'requests>=2.25.1',
        # 'pandas>=1.2.0',
    ],
    extras_require={
        "dev": [
            "black",
            "isort",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={"stock_info": ["VERSION"]},
    python_requires=">=3.10",
)
