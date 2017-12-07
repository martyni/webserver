# Web app vagrant box

This Vagrant file brings up 4 servers

 * Mongo Db server
 * 2 Flask app servers
 * 1 ansible controller that also acts as an nginx proxy server

The project should come up with 

```
vagrant up

```

I had some difficulties getting ansible_local to work so the servers are provisioned with a SHELL command that starts an
ansible playbook on the controller instance.
The ansible environment is inside a python virtual environment (/home/vagrant/ansible/bin/activate) as I was having an issue getting it installed any other way. [This](https://github.com/ansible/ansible/issues/31741) is where I found the solution I implemented.

If you want to rerun the ansible script this is the easiest way to do it.

```
vagrant provision controller

```

I spent 2 evenings working on this project (about 8 hours).
This is my local vagrant environment
```
vagrant-share (1.1.8, system)
vagrant-vbguest (0.13.0)
```

## Some notes
* Only the controller server gets the user modifications (admin group etc) applied to it.
* The mongo populator script will duplicate entries if mongo server is stopped and automation re-run
* The app servers have to come up after the db servers otherwise they will crash
* Access to the node servers (e.g not the controller) is provided via a hard set password. This is set in a short shell script when the servers are booted.
* Originally I had an ``` apt-get upgrade ``` when I provisioned the nodes but this made the process take a long time (in excess of half an hour) so I removed it.
* The servers are provisioned by hard setting their IPs. I tried to pick a random subnet to put them in but if 192.168.33.0/24 is in use in your local network then this project may fail (They're mentioned soley within the Vagrant file so you'd just need to change them in there)
* Docs are written in Github flavoured markdown
