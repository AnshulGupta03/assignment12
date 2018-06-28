#Q1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc). 
'''
An access token is an object that describes the security context of a process or thread. The information in a token includes the identity and privileges of
the user account associated with the process or thread. When a user logs on, the system verifies the user's password by comparing it with information stored
in a security database. If the password is authenticated, the system produces an access token. Every process executed on behalf of this user has a copy of this access token.
'''


#Q1.(REPLACED)Difference between JSON And XML
'''
A list of differences between JSON and XML are given below.

No.	JSON	                                            XML
1)	JSON stands for JavaScript Object Notation.	    XML stands for eXtensible Markup Language.
2)	JSON is simple to read and write.	            XML is less simple than JSON.
3)	JSON is easy to learn.	                            XML is less easy than JSON.
4)	JSON is data-oriented.	                            XML is document-oriented.
5)	JSON doesn't provide display capabilities.	    XML provides the capability to display data because it is a markup language.
6)	JSON supports array.	                            XML doesn't support array.
7)	JSON is less secured than XML.	                    XML is more secured.
8)	JSON files are more human readable than XML.	    XML files are less human readable.
9)	JSON supports only text and number data type.	    XML support many data types such as text, number, images, charts, graphs etc. Moreover, XML offeres options for transferring the format or structure of the data with actual data.
'''


#Q2.Get the IP address of some common sites like Google, Facebook by using DNS lookup.

import socket

addr1 = socket.gethostbyname('google.com')
addr2 = socket.gethostbyname('yahoo.com')
addr3 = socket.gethostbyname('facebook.com')
addr4 = socket.gethostbyname('twitter.com')

print("IP address of google is ",addr1)
print("IP address of yahoo is ",addr2)
print("IP address of facebook is ",addr3)
print("IP address of twitter is ",addr4)




#Q3.Working of http(get,pot,put,delete)

'''
Whenever a client submits a request to a server, part of that request is an HTTP method, which is what the client would like the server to do with the specified resource.
HTTP methods represent those requested actions. For example, some commonly-used HTTP methods will retrieve data from a server, submit data to a server for processing,
delete an item from the server's data store, etc.

#get          
GET requests are the most common and widely used methods in APIs and websites. Simply put, the GET method is used to retreive data from a server at the specified resource.
For example, say you have an API with a /users endpoint. Making a GET request to that endpoint should return a list of all available users.
Since a GET request is only requesting data and not modifying any resources, it's considered a safe and idempotent method.

#post
POST requests are used to send data to the API sever to create or udpate a resource. The data sent to the server is stored in the request body of the HTTP request.
The simplest example is a contact form on a website . When you fill out the inputs in a form and hit Send, that data is put in the response body of the request and sent to the server.
This may be JSON, XML, or query parameters (there's plenty of other formats, but these are the most common).

#put
Simlar to POST, PUT requests are used to send data to the API to create or update a resource. The difference is that PUT requests are idempotent.
That is, calling the same PUT request multiple times will always produce the same result. In contrast, calling a POST request repeatedly make have side
effects of creating the same resource multiple times.

#delete
The DELETE method is exactly as it sounds: delete the resource at the specified URL. This method is one of the more common in RESTful APIs so it's good to know how it works.

If a new user is created with a POST request to /users, and it can be retrieved with a GET request to /users/{{userid}}, then making a DELETE request to /users/{{userid}} will completely remove that user.
                                                                                                                                                                                                                                   
'''




#Q4.What is a difference between library and API . Figure it out with examples.
'''
A library is a chunk of code designed for reuse that is typically installed locally. A library is most often wrapped in an API that defines the functionality the library
provides and how to use it.

API refers to an interface that doesn't need to have an implementation. However, when people speak of an API they are usually referring to a reusable library or service.
Where a library is used as a package of code, a service is a running system that provides functionality to other systems and applications.
'''


