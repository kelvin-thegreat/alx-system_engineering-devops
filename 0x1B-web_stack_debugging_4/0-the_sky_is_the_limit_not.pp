# Increase the amount of traffic an Nginx server can handle.
# let’s fix our stack so that we get to 0
exec { 'fix--for-nginx':
  # Run sed command to replace the value '15' with '4096' in the /etc/default/nginx file
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx through exectuion of nginx service restart command
exec { 'nginx-restart':
  command => 'sudo service nginx restart',
  path    => '/etc/init.d/'
}
