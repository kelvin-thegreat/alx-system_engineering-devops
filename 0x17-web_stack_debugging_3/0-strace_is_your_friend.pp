# Fix bad .phpp to .php : Why Apache is returning a 500 error
# file { '/var/www/html/wp-settings.php':
#  ensure  => file,
#  content => template('my_module/wp-settings.php.erb'),
#  require => Exec['fix-wordpress'],
# }
}
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
service { 'apache2':
  ensure => 'running',
  notify => Exec['fix-wordpress'],
}
