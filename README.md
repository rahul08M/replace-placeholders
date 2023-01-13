# replace-placeholders

#### A method to replace placeholders or variable placed into the string.

```
# string : Hey, {{var:ninja_name:'Ninja'}} show me your justu !!!
# used variable : {{var:ninja_name:'Ninja'}}. Here var is keyword ninja_name is variable name and 
'Ninja' is the default value.
# replace_variables() method required two parameters, the input string (string) and variables data (dict)

input 1
replace_variables("Hey, {{var:ninja_name:'Ninja'}} show me your justu !!!", {'ninja_name': 'Kakashi'})
>>> Hey, Kakashi show me your justu !!!

input 2
replace_variables("Hard work is worthless for those that don't believe in themselves. – {{var:ninja_name:'Ninja'}}", {'ninja_name': 'Naruto Uzumaki'})
>>> Hard work is worthless for those that don't believe in themselves. – Naruto Uzumaki
```
