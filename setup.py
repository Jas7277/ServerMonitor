from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="server-monitor",
    version="1.0.0a",
    author="Jas7277",
    description="Lightweight Flask-based agent to monitor server metrics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jas7277/ServerMonitor",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Monitoring",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "server-monitor=server_monitor.agent:main",
        ],
    },
    include_package_data=True,
    package_data={
        "server_monitor": [
            "templates/*.html",
            "static/css/*.css",
            "static/js/*.js",
        ],
    },
)
