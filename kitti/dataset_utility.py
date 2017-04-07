## Currently loadcalibrationcamtocam and loadcalibrationrigid are exactly same
# Expand functionality in the future?
def parse_string_variable(str):
    var_name = str.split(':')[0]
    after_colon_index = len(var_name) + 1
    value = str[after_colon_index:]
    return (var_name, value)

def read_lines_to_dict(raw_text):
    var_list = []
    for i, line in enumerate(raw_text):
        var_list.append(line.replace('\n', ''))
    for i, line in enumerate(raw_text):
        var_list[i] = parse_string_variable(line)
    return dict(var_list)

def read_files_by_lines(filename):
    assert type(filename) is str
    with open(filename, 'r') as cam_to_cam:
#         data = cam_to_cam.read().replace('\n', 'r')
        data = cam_to_cam.readlines()
    return read_lines_to_dict(data)


def loadCalibrationCamToCam(filename, verbose=False):
    assert type(filename) is str
    cam_dict = read_files_by_lines(filename)

    for key, value in cam_dict.items():
        if key == 'calib_time':
            cam_dict[key] = value
            if verbose:
                print(key, value)
        else:
            array = []
            for i, string in enumerate(value.split(' ')[1:]):
                array.append(float(string))
            cam_dict[key] = array
            if verbose:
                print(key, array)
    return cam_dict

def loadCalibrationRigid(filename, verbose=False):
    assert type(filename) is str
    velo_dict = read_files_by_lines(filename)

    for key, value in velo_dict.items():
        if key == 'calib_time':
            velo_dict[key] = value
            if verbose:
                print(key, value)
        else:
            array = []
            for i, string in enumerate(value.split(' ')[1:]):
                array.append(float(string))
            velo_dict[key] = array
            if verbose:
                print(key, array)
    return velo_dict
