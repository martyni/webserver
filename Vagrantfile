# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.define "app1" do |app|
     app.vm.box = "puppetlabs/ubuntu-14.04-64-nocm"
     app.vm.network "private_network", ip: "192.168.33.11"
     app.vm.provision "shell", inline: <<-SHELL
     echo -e "vagrant\nvagrant\n" | passwd vagrant
     SHELL
  end   
  config.vm.define "app2" do |app|
     app.vm.box = "puppetlabs/ubuntu-14.04-64-nocm"
     app.vm.network "private_network", ip: "192.168.33.12"
     app.vm.provision "shell", inline: <<-SHELL
     echo -e "vagrant\nvagrant\n" | passwd vagrant
     SHELL
  end   
  config.vm.define "db" do |db|
     db.vm.box = "puppetlabs/ubuntu-14.04-64-nocm"
     db.vm.network "private_network", ip: "192.168.33.13"
     db.vm.provision "shell", inline: <<-SHELL
     echo -e "vagrant\nvagrant\n" | passwd vagrant
     SHELL
  end   
  config.vm.define "controller" do |controller|
     controller.vm.box = "puppetlabs/ubuntu-14.04-64-nocm"
     controller.vm.network "private_network", ip: "192.168.33.10"
     controller.vm.box = "puppetlabs/ubuntu-14.04-64-nocm"
     controller.vm.network "private_network", ip: "192.168.33.10"
     controller.vm.provision "shell", inline: <<-SHELL
       if [ -e /root/init ]
         then 
            echo "Skipping setup"
            source ansible/bin/activate
       else 
          apt-get update
          apt-get install -y python-pip sshpass
          pip install virtualenv
          virtualenv ansible
          source ansible/bin/activate
          pip install --upgrade setuptools
          pip install cffi
          pip install ansible
          ssh-keygen -f "/root/.ssh/id_rsa" -t rsa -N ""
          cat /root/.ssh/id_rsa.pub >>/home/vagrant/.ssh/authorized_keys
	  mkdir -p /etc/ansible/
	  for host in localhost 192.168.33.11 192.168.33.12 192.168.33.13
             do 
	       ssh-keyscan -H $host >> ~/.ssh/known_hosts
	  done
          cat > /etc/ansible/hosts << EOF
[app]
192.168.33.11 ansible_user=vagrant ansible_ssh_pass=vagrant
192.168.33.12 ansible_user=vagrant ansible_ssh_pass=vagrant

[db]
192.168.33.13 ansible_user=vagrant ansible_ssh_pass=vagrant

[controller]
localhost ansible_user=vagrant
EOF
          touch /root/init
       fi
       cd /vagrant
       ansible-playbook site.yml
       echo " " 
       echo "VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV"
       test_pass(){
          echo $1
       }
       test_fail() {
          echo $1
          exit 1
       }
       echo Starting tests
       curl -s localhost>/dev/null && test_pass "Webserver up woohoo" || test_fail "Webserver down boo"
       for host in  192.168.33.11:5000 192.168.33.12:5000
         do curl -s $host>/dev/null && test_pass "Appserver $host up woohoo" || test_fail "Appserver $host down boo"
       done
       echo Check website at http://192.168.33.10
     SHELL
  end   
end
