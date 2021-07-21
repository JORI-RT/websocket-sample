Vagrant.configure("2") do |config| 
    config.vm.box = "centos/7"
  config.vm.define :lb do |node|
    node.vm.network :private_network, ip:"192.168.33.200"
    node.vm.hostname = "lb.local"
  end
  config.vm.define :app1 do |node|
    node.vm.network :private_network, ip:"192.168.33.201"
    node.vm.hostname = "app1.local"
  end
  config.vm.define :app2 do |node|
    node.vm.network :private_network, ip:"192.168.33.202"
    node.vm.hostname = "app2.local"
  end
  config.vm.define :pubsub do |node|
    node.vm.network :private_network, ip:"192.168.33.203"
    node.vm.hostname = "pubsub.local"
  end
end