file_list = range(1,11)
time_interval = 50

src_add = '134.197.41.42'
# src_add = '134.197.113.69'
dst_add = '134.197.113.68'
def get_input():
    inputs = { 'file_list': file_list,
              'time_interval': time_interval,
               'src_add': src_add,
               'dst_add': dst_add
            }
    return inputs
