# Install Nginx server and setup and configuration Using Puppet

package { 'nginx':
  ensure => 'installed'
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'redirection-301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://x.com/Ali_Taha_AMT permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
