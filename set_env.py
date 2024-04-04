def set_env(host):
    host.cmd('export PATH=$PATH:/usr/local/go/bin')
    host.cmd('export OPENSSL_CONF=/home/parallels/quantumsafe/build/ssl/openssl.cnf')
    host.cmd('export OPENSSL_MODULES=/home/parallels/quantumsafe/build/lib')
    host.cmd('export WORKSPACE=/home/parallels/quantumsafe')
    host.cmd('export BUILD_DIR=$WORKSPACE/build ')
    host.cmd('export LD_LIBRARY_PATH=/home/parallels/quantumsafe/liboqs/build/lib')
    host.cmd('export PKG_CONFIG_PATH=/home/parallels/quantumsafe/liboqs-go/.config')