# Set up server configuration with puppet
file_line{'Set alias name':
  path => '/etc/ssh/ssh_config',
  line => 'Host 35.153.50.198
    HostName 35.153.50.198
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
