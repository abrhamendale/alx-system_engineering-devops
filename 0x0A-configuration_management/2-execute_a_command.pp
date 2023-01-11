# Executes the pkill command on killmenow process
exec { 'pkill killmenow' :
  path => '/usr/bin',
  }
