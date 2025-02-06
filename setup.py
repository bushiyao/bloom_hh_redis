from setuptools import setup, find_packages

setup(
    name="bloom_filter_redis",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "redis",
        "redisbloom-py",
    ],
    author="bushiyao_",
    author_email="1048493533@qq.com",
    description="Redis-backed Bloom Filter implementation",
    url="https://github.com/bushiyao/bloom_hh_redis",
)