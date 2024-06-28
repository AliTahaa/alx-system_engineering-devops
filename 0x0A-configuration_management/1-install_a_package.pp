# Install an especific version of flask (2.1.0)
class { 'python::pip': }  # Include the python::pip class

pip { 'flask':
  ensure => '2.1.0',  # Specify desired version
  provider => 'pip3',  # Explicitly use pip3 provider
}
