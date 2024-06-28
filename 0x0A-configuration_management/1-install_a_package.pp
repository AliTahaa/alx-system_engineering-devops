# Install an especific version of flask (2.1.0)
class { 'python::pip': }

pip { 'flask':
  ensure => '2.1.0',
}
