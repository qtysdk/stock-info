from setuptools import setup, find_packages

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
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
