import redis
from redisbloom.client import Client

class RedisBloomFilter:
    def __init__(self, name='bloom_filter', host='localhost', port=6379, db=0, error_rate=0.001, capacity=1000):
        self.name = name
        self.client = Client(host=host, port=port, db=db)
        # 初始化布隆过滤器（如果不存在）
        self.client.bfCreate(name, error_rate, capacity)

    def add(self, item):
        """添加元素到布隆过滤器"""
        return self.client.bfAdd(self.name, item)

    def exists(self, item):
        """检查元素是否存在"""
        return self.client.bfExists(self.name, item)

# 示例用法
if __name__ == "__main__":
    # 连接到本地 Redis
    bf = RedisBloomFilter(name="my_bloom_filter", error_rate=0.001, capacity=10000)
    bf.add("example")
    print(bf.exists("example"))  # 输出 1（存在）
    print(bf.exists("nonexistent"))  # 输出 0（不存在）