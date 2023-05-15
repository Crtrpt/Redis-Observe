import redis


cli=redis.cluster.RedisCluster("127.0.0.1",6379)

print(cli.set("aa","test"))
print(cli.set("ab","test"))
print(cli.set("ac","test"))
print(cli.get("aa"))

