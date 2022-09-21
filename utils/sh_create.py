import os


def sh_create(sh_name, hyper_param):
    """
    传入超参数，建立Linux下的运行脚本
    Args:
        hyper_param: 超参数表，为一个json对象
    Return:
        无
    """
    if not os.path.exists(".\\sh\\"):
        os.mkdir(".\\sh\\")
    with open(".\\sh\\" + sh_name, "w", encoding='utf8') as f:
        f.write("python3 " + hyper_param["train_file"] + " \\" + "\n")
        for i in hyper_param:
            if i is not "train_file" and i is not "project":
                f.write("\t")
                f.write("--" + i + "=")
                if i is "device":
                    f.write("cuda")
                else:
                    f.write(str(hyper_param[i]))
                f.write(" \\")
                f.write("\n")
    with open(".\\sh\\" + sh_name, "rb+") as f2:
        f2.seek(-4, os.SEEK_END)
        f2.truncate()


def json_create(argparse):
    return argparse.__dict__


if __name__ == '__main__':
    test_json = {
        "batch_size": 32,
        "lr": 1e-3,
        "input_size": 300,
        "hidden_size": 300,
        "train_file": "train.py",
    }
    sh_create("test.sh", test_json)
