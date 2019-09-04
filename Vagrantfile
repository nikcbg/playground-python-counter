Vagrant.configure("2") do |config|
  config.vm.box = "nikcbg/ubuntu16-redis"
  config.vm.box_version = "0.1"
  config.vm.hostname = "redis64"
  config.vm.network "private_network", ip: "192.168.1.10"
  config.vm.network "forwarded_port", guest: 6379, host: 6379 
  config.vm.provision :shell, path: "scripts/provision.sh"
end
