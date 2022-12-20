keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
 
new_dict = {keys: values for keys,
            values in zip(keys, values)}
print(new_dict)