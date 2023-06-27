# Installation of Engine X using puppet

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'apt-get update ; apt-get -y install nginx',
  provider => shell,

}

exec {'Hello':
  command  => 'echo "Hello World!" | tee /var/www/html/index.html',
  provider => shell,
}

exec {'sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/blog.ehoneahobed.com\/;\\n\\t}/" /etc/nginx/sites-available/default':
  provider => shell,
}

exec {'run':
  command  => 'service nginx restart',
  provider => shell,
}
