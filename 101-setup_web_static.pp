# This script sets up webservers for the deployment of the webstatic

# Update and install nginx if it doesnt exist
exec {'update':
  provider => shell,
  command  => 'apt-get -y update',
}

package {'nginx':
  ensure   => installed,
  provider => 'apt',
}

# create folders if they don't exist exits
file {'test':
  ensure => directory,
  path   => '/data/web_static/releases/test/',
}

file {'shared':
  ensure => directory,
  path   => '/data/web_static/shared/',
}

# create an html file with fake content to test configuration
exec {'index':
  provider => shell,
  command  => 'echo -e "<html>\\n\\t<head>\\n\\t</head>\\n\\t<body>\\n\\t\\t<h1>Hello ALX</h1>\\n\\t</body>\\n</html>" > /data/web_static/releases/test/index.html',
}

# remove the symbolic link if exist and recreate it
exec {'update':
  provider => shell,
  command  => 'rm -rf /data/web_static/current; ln -s /data/web_static/releases/test/ /data/web_static/current',
}

# give ownership to the user and group ubuntu
exec {'ownership':
  provider => shell,
  command  => 'chown -R ubuntu:ubuntu /data/',
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# update the nginx config the content of /data/web_static/current/ to hbnb_static
exec {'update-config':
  provider => shell,
  command  =>'sed -i "s/^\\s*location \\/ {/\\tlocation \\/hbnb_static {\\n\\t\\talias \\/data\\/web_static\\/current\\/;\\n\\t}\\n\\n&/" /etc/nginx/sites-enabled/default',
}

# restart the server
exec {'restart':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => Service['nginx'],
}
