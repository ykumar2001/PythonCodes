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



def final_result(r):
    for key ,value in r.items():
        if isinstance(value,dict):
            final_result(value)
        elif isinstance (value,int):
            print(f"{key} : {value}") 
print("output:")
final_result(d1)
