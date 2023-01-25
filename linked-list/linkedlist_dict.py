head =  {
    'value':11,
    'next': {
        'value':3,
        'next': {
            'value':23,
            'next': {
                'value':7,
                'next': {
                    'value':4,
                    'next': None # <- tail
                    }
                }
            }
        }
    }

print(head['next']['next']['value'])
# 23


# If it was a linked list we would use this print statement:
# print(my_linked_list.head.next.next.value)


'''
print   (                 head   ['next'] ['next'] ['value'] )
print   ( my_linked_list. head.    next.    next.    value   )
'''

