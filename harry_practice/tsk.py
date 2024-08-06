d1={
    'key_1_0': {
        'key_2_0': {
            'key_3_0': {
                'key_4_0': {
                    'key_5_0': 23
                },
                'key_4_1': 95
            },
            'key_3_1': 17
        },
        'key_2_1': {
            'key_3_0': 32
        }
    },
    'key_1_1': {
        'key_2_0': {
            'key_3_0': 50
        }
    }
} 




# def print_last_values(d):
#     if isinstance (d,dict):
#         for key,value in d.items():
#             if isinstance(value,dict):
#                 print_last_values(value)
#         last_key=list(d.keys())[-1]
#         last_value=d[last_key]
#         if not isinstance(last_value,dict):
#             print(f"{last_key}:{last_value}")
# print("output:")
# print_last_values(d1)                    

def print_last_value(d):
    for key, value in d.items():
        if isinstance(value,dict):
            print_last_value(value)
        elif isinstance(value,(int,float)):
            print(f"{key}:{value}")
print("output:")
print_last_value(d1)                