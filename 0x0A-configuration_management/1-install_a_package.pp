# Installs flask using pip3
package { 'flask-2.1.0':
  ensure   => installed,
  provider => pip3,
}
