# 自定义过滤器,判断index位置,如果是1,返回clss1

def do_class_index(index):

    if index == 0:
        return "first"
    elif index == 1:
        return "second"
    elif index == 2:
        return "third"
    else:
        return ""