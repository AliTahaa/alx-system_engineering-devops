#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
yumrepo { 'epel':
  baseurl => 'https://dl.fedoraproject.org/pub/epel/8/x86_64/',
  enabled => yes,
}

package { 'python38':
  ensure => present,
}

class { 'python::pip': }

pip { 'flask':
  ensure => '2.1.0',
  provider => 'pip3',
}

pip { 'Werkzeug':
  ensure => '2.1.1',
  provider => 'pip3',
  require => Package['flask'],
}
