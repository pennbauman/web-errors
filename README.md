# Web Errors
Python script to auto generate web server error pages. 

## Use
1. Setup template.shtml, this can be done with:

	cp sample-template.shtml template.shtml

Templates accept 3 variables formated as `{{var}}` to input text into the page based on the error:

	* `{{code}}` For the error code (i.e. '404').
	* `{{title}}` For the name of the error (i.e. 'Page Not Found').
	* `{{body}}` For a description of the error.

2. Run:

	python error-gen.py

3. Collect the error files from output/ and move them to your web server

## Setting Up Error Files
Add the following lines to .htaccess on your server, substitute file locations as appropriate:

	ErrorDocument 400 /errors/400.shtml
	ErrorDocument 401 /errors/401.shtml
	ErrorDocument 401 /errors/402.shtml
	ErrorDocument 403 /errors/403.shtml
	ErrorDocument 404 /errors/404.shtml
	ErrorDocument 401 /errors/405.shtml
	ErrorDocument 401 /errors/406.shtml
	ErrorDocument 401 /errors/407.shtml
	ErrorDocument 401 /errors/408.shtml
	ErrorDocument 401 /errors/409.shtml
	ErrorDocument 401 /errors/410.shtml
	ErrorDocument 401 /errors/411.shtml
	ErrorDocument 401 /errors/412.shtml
	ErrorDocument 401 /errors/413.shtml
	ErrorDocument 401 /errors/414.shtml
	ErrorDocument 401 /errors/415.shtml
	ErrorDocument 401 /errors/416.shtml
	ErrorDocument 401 /errors/417.shtml
	ErrorDocument 401 /errors/422.shtml
	ErrorDocument 401 /errors/423.shtml
	ErrorDocument 401 /errors/424.shtml
	ErrorDocument 500 /errors/500.shtml
	ErrorDocument 500 /errors/501.shtml
	ErrorDocument 500 /errors/502.shtml
	ErrorDocument 500 /errors/503.shtml
	ErrorDocument 500 /errors/504.shtml
	ErrorDocument 500 /errors/505.shtml
	ErrorDocument 500 /errors/506.shtml
	ErrorDocument 500 /errors/507.shtml
	ErrorDocument 500 /errors/510.shtml
