# URL lookup service 

######################
Challange
######################
We have an HTTP proxy that is scanning traffic looking for malware URL's. Before allowing HTTP connections to be made, 
this proxy asks a service that maintains several databases of malware URL's if the resource being requested is known to 
contain malware.  Write a small web service, preferably in Python or Ruby, that responds to GET requests where the 
caller passes in a URL and the service responds with some information about that URL. The GET requests would look like 
this:   
GET /urlinfo/1/{hostname_and_port}/{original_path_and_query_string}   


The caller wants to know if it is safe to access that URL or not. As the implementor you get to choose the response 
format and structure. These lookups are blocking users from accessing the URL until the caller receives a response from 
your service. 
 
 
Challenges:
1. The size of the URL list could grow infinitely, how might you scale this beyond the memory capacity of the 
system? Bonus if you implement this.  
2. The number of requests may exceed the capacity of this system, how might you solve that? Bonus if you implement this.
3, What are some strategies you might use to update the service with new URLs? Updates may be as much as 5 thousand 
URLs a day with updates arriving every 10 minutes.


######################
Info on URL Lookup Service
######################
URL_Lookup.py : Main backend module that parses URL from application request, looks up in mysql db for malwares
                returns the result with URL is safe or Malware.
update_db_with_malwares.py: Backend module to update service's database periodically with the info about new URLs or 
                updates on existing URLs.
URL_Lookup_WHOIS.py: Alternative URL info source WHOIS registars

URL_Lookup_App.py: Example Application using this URL Lookup service to verify it's safe to visit URL before visiting.
simple.html:    An html webform accepting URL and calls backend module with cgi field to consume the backend service.                                

######################
How to Use???
######################
1. Place the simple.html file under your webserver's config
    Example: MAMP ===>> /Applications/MAMP/htdocs
2. Checkout everything else and keep it under your webserver's cgi-bin config
    Example: MAMP ===>> /Applications/MAMP/cgi-bin

WS would look like this
bash-3.2$ ls -lrt
total 24
-rwxr-xr-x  1 jigasha2  admin  670 Sep  7 16:20 URL_Lookup_App.py
drwxr-xr-x  7 jigasha2  admin  238 Sep  7 16:33 URL-Lookup
bash-3.2$ pwd
/Applications/MAMP/cgi-bin