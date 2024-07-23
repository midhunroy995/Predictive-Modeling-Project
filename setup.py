from setuptools import setup, find_packages

setup(
    name="HousePricePrediction",
    version="0.1",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'pyyaml',
        'jupyter',
    ],
    entry_points={
        'console_scripts': [
            # Define command-line tools here if needed
            # Example:
            # 'housepricepredict=src.HousePricePrediction.main:main',
        ],
    },
    include_package_data=True,
    description="A project for predicting house prices using machine learning.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/midhunroy995/Predictive-Modeling-Project.git",
    author="midhunroy995",
    author_email="midhunroy7510@gmail.com",
    license="MIT",
)

