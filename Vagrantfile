VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/bionic64"

  config.vm.define "web1" do |web1|
    web1.vm.hostname = "web1"
    web1.vm.network "private_network", ip: "192.168.59.11"
  end

  config.vm.define "app1" do |app1|
    app1.vm.hostname = "app1"
    app1.vm.network "private_network", ip: "192.168.59.12"
  end

  config.vm.define "app2" do |app2|
    app2.vm.hostname = "app1"
    app2.vm.network "private_network", ip: "192.168.59.15"
  end


  config.vm.define "db1" do |db1|
    db1.vm.hostname = "db1"
    db1.vm.network "private_network", ip: "192.168.59.13"
  end
end
