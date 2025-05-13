def common_prefix(given_list):
    if len(given_list) == 0:
        return ''
    prefix = given_list[0]
    for word in given_list:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if len(prefix) == 0:
                return ''
    return prefix

given_list = ['aravind','arun','arjun']
print(common_prefix(given_list))

