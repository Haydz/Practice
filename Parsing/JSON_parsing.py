#what it is:
#JSON feeds can be loaded asynchronously much more easily than XML/RSS.
#https://www.copterlabs.com/json-what-it-is-how-it-works-how-to-use-it/
#http://docs.python-guide.org/en/latest/scenarios/json/
"""
JSON is short for JavaScript Object Notation, and is a way to store
information in an organized, easy-to-access manner. In a nutshell,
it gives us a human-readable
collection of data that we can access in a really logical manner.
With the rise of AJAX-powered sites, it's becoming more
and more important for sites to be able to load data quickly
and asynchronously, or in the background without delaying page rendering.


"""
"""

most basic
var jason = {
	"age" : "24",
	"hometown" : "Missoula, MT",
	"gender" : "male"
};

Object = Jason
name value paring.

within JSON:
document.write('Jason is ' jason.age);

Can have multiple objects in one variable
ARRAYS:


var family = [{
    "name" : "Jason",
    "age" : "24",
    "gender" : "male"
},
{
    "name" : "Kyle",
    "age" : "21",
    "gender" : "male"
}];

TO ACCESS:
document.write(family[1].name); // Output: Kyle
document.write(family[0].age); // Output: 24

CAN NEST OBJECTS
var family = {
    "jason" : {
        "name" : "Jason Lengstorf",
        "age" : "24",
        "gender" : "male"
    },
    "kyle" : {
        "name" : "Kyle Lengstorf",
        "age" : "21",
        "gender" : "male"
    }
}

"""
#playing with JSON

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

import json
parsed_json = json.loads(json_string)

#normal dictionary
print parsed_json['first_name']

"""Can create json data as well:

"""

d = {
    'first_name' : 'Guido',
    'second_name' : 'Rossum',
    'Titles' : ['BDFL', 'Developer']
}
#need to convert back to json
b = json.dumps(d)
c = json.loads(b)
print c
#does not act as p
print type(c)
print c['first_name']
