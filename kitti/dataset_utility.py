import numpy as np
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

def replace_var_from_dict_with_shape(var_dict, key, shape):
    var_dict[key] = np.array(var_dict[key]).reshape(shape)

def loadCalibrationCamToCam(filename, verbose=False):
    assert type(filename) is str
    cam_dict = read_files_by_lines(filename)

    for key, value in cam_dict.items():
        if key == 'calib_time':
            cam_dict[key] = value
        else:
            array = []
            for i, string in enumerate(value.split(' ')[1:]):
                array.append(float(string))
            cam_dict[key] = array

    for i in range(0, 4):
        S_rect_0i = 'S_rect_0' + str(i)
        R_rect_0i = 'R_rect_0' + str(i)
        P_rect_0i = 'P_rect_0' + str(i)
        S_0i = 'S_0' + str(i)
        K_0i = 'K_0' + str(i)
        D_0i = 'D_0' + str(i)
        R_0i = 'R_0' + str(i)
        T_0i = 'T_0' + str(i)

        replace_var_from_dict_with_shape(cam_dict, S_rect_0i, (1, 2))
        replace_var_from_dict_with_shape(cam_dict, R_rect_0i, (3, 3))
        replace_var_from_dict_with_shape(cam_dict, P_rect_0i, (3, 4))
        replace_var_from_dict_with_shape(cam_dict, S_0i, (1, 2))
        replace_var_from_dict_with_shape(cam_dict, K_0i, (3, 3))
        replace_var_from_dict_with_shape(cam_dict, D_0i, (1, 5))
        replace_var_from_dict_with_shape(cam_dict, R_0i, (3, 3))
        replace_var_from_dict_with_shape(cam_dict, T_0i, (3, 1))

    if verbose:
          print(S_rect_0i, cam_dict[S_rect_0i])
          print(R_rect_0i, cam_dict[R_rect_0i])
          print(P_rect_0i, cam_dict[P_rect_0i])
          print(S_0i, cam_dict[S_0i])
          print(K_0i, cam_dict[K_0i])
          print(D_0i, cam_dict[D_0i])
          print(R_0i, cam_dict[R_0i])
          print(T_0i, cam_dict[T_0i])
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
