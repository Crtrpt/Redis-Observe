
# mac如果make 报错 更新make 版本 /usr/local/opt/make/libexec/gnubin
all: build_RedisTimeSeries build_RedisJson build_RedisSearch build_RedisGraph build_redlock

build_RedisTimeSeries:
	cd RedisTimeSeries && git submodule update --init --recursive && make

build_RedisJson:
	cd RedisJson && git submodule update --init --recursive && make

build_RedisSearch:
	cd RedisSearch && git submodule update --init --recursive && make

build_RedisGraph:
	cd RedisGraph && git submodule update --init --recursive && make

build_redlock:
	cd redlock && git submodule update --init --recursive && make