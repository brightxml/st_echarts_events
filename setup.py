import setuptools
from os import path

dir = path.abspath(path.dirname(__file__))
with open(path.join(dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setuptools.setup(
    name="st-echarts-events",
    version="1.0.0",
    author="隐园",
    author_email="brightxml@gmail.com",
    description="A custom streamlit component to return echarts events values to streamlit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brightxml/st_echarts_events",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63"
    ],
)
