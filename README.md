# Learn_Coding_With_Python
Using list in python
## You can change list data type 
* List usage
  * name = list()
  * name.append("hello")
  * name.append(12)
  * ['hello',12]
* [ rstrip()](https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_rstrip)
## Join  lists of list by using 
``` 
    x = [["a","b"], ["c"]] 
    result = sum(x, [])
```
## Identify-duplicate-values-in-a-list
**[Reference](https://stackoverflow.com/questions/11236006/identify-duplicate-values-in-a-list-in-python)

```
     [newlist[i] for i in range(len(newlist)) if i == newlist.index(newlist[i])])
```
