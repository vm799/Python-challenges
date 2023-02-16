"""
Creating a dictionary contact list
a - c
"""

contact_list = {
    "a" :{
        "anne" : "0879874932472",
        "annie" : "0879874932472",
        "anne-may" : "0879874932472"
    },
    "b" :{
        "bob" : "2087987493432472"
    },
    "c" :{
        "cezanne" : "30879874932472"
    },
    "d" :{
        "dianne" : "70879874932472"
    },
    "e" :{
        "evanne" : "90879874932472"
    }
    
}

contact_list["b"]["bobby"] =  "4234243"
print(contact_list["a"].pop("annie"))
print(contact_list.get("d"))

theList = []
theList.append(1234)
print(theList)
theList.append(4567)
print(len(theList))




