#!/bin/bash

# Update apt
apt-get update

# Install packages we need:
#
#   - python-setuptools: to easy_install pip
#   - python-dev: development headers so we can compile python C extensions
#   - libpq-dv: PostgreSQL client library headers so we can compile
#       psycopg
#   - libevent-dev: for guinicorn
#   - git-core: So we can work with git
#   - curl: Useful debugging tool
#   - pep8, pyflakes: Useful dev tools for Python
#   - make: Everything needs make.
#   - htop: Useful ops tool.
apt-get install -y \
  python-setuptools \
  python-dev \
  libpq-dev \
  libevent-dev \
  git-core \
  curl \
  pep8 \
  pyflakes \
  make \
  htop

# For Python dependencies, run `make deps` to install them
easy_install pip

# Automatically move into the shared folder, but only add the command
# if it's not already there.
grep -q 'cd /vagrant' /home/vagrant/.bash_profile || echo 'cd /vagrant' >> /home/vagrant/.bash_profile

# For running a web application like Heroku does
curl https://godist.herokuapp.com/projects/ddollar/forego/releases/current/linux-amd64/forego -o /usr/local/bin/forego
chmod +x /usr/local/bin/forego

echo "

Provisioning Complete. CTRL+C if this shows for more than a few seconds...

"
