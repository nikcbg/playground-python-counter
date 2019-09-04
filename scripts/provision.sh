grep "bind 0.0.0.0" /etc/redis/redis.conf || {
  cp /etc/redis/redis.conf /etc/redis/redis.conf.back
  cp /vagrant/conf/redis.conf /etc/redis/redis.conf
  systemctl restart redis-server
}
