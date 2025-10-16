ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#list items are ordered, changeable and allow duplicate values -> can swap value by index
ft_list[1] = "World!"

#tupe items are ordered, unchangeable and allow duplicate values
#We must create a list to change a value of a tupe, like below
tmp = list(ft_tuple)
tmp[1] = "France!"
ft_tuple = tuple(tmp)

#set items are unordered, unchangeable and do not allow duplicate values
#We must use a manual method to remove and add values
#set is unordered, so we can't manipulate the output
ft_set.add("Angouleme!")
ft_set.remove("tutu!")

#dictionaries are ordered, changeable and do not allow duplicate 
#it store datas and keys in format {"Data" : "Key"} like a map in cpp
ft_dict["Hello"] = "42Angouleme!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)