import os


def _combine_keys_values(dict_, combine_str=''):
    result = []
    for k, v in dict_.items():
        for v_i in v:
            result.append(k+combine_str+v_i)
    return result


def get_files(path_root, combine=False):
    '''
    return a dict of files in the path_root, 
    if combine is True, return a list of files with relative path
    '''
    result = {}
    list_ = os.listdir(path_root)
    for list_i in list_:
        path = os.path.join(path_root, list_i)

        # recurse into sub-dirs
        if os.path.isdir(path):
            result.update(get_files(path))

        if os.path.isfile(path):
            if os.path.split(path)[0] not in result.keys():
                result[os.path.split(path)[0]] = []
            result[os.path.split(path)[0]].append(os.path.split(path)[1])

    if combine:
        return _combine_keys_values(result, '\\')
    return result


