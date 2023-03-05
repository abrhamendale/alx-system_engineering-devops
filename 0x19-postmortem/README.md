Postmortem
Website not loading

1. Issue Summary: On March 4 at 9:00 EAT Website was unresponsive with a returned response code 500 when trying to access through browser. No user was able to access the site at the time. At 10:00 EAT, found the problem. At 10:30 EAT, the problem was fixed and the website was functional.
2. Timeline: At 9:00 EAT it was reported by the customers that the website could not load, prompting the website team to troubleshoot the issue by checking for hardware problems, the load balancer, checking the log files. It was found that the nginx service was not running when the loopback address was used to access the site and restarting the service corrected the issue.
3. Root cause and resolution: Nginx was accidentally stopped due to another installation
4. Corrective and preventative measures: checkup when changes are made to the server



                      5 5 5 5 5 5 5 5                    0 0 0 0 0 0 0                    5 5 5 5 5 5 5 5
                    5                                  0               0                5                
                    5                                 0                 0               5
                    5                                 0                 0               5
                    5   5 5 5 5 5 5                   0                 0               5   5 5 5 5 5 5 
                    5 5             5                 0                 0               5 5             5 
                    5                 5               0                 0               5                 5
                                      5               0                 0                                 5 
                                      5               0                 0                                 5 
                                      5               0                 0                                 5
                                    5                   0             0                                 5 
                        5 5 5 5 5 5                       0 0 0 0 0 0                      5 5 5 5 5 5 