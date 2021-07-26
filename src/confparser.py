import configparser
def parse(var):
    cfg = configparser.ConfigParser()
    cfg.read('../vars.conf')
    return cfg['DEFAULT'][var]


def parse_path(path,header, var):
    cfg = configparser.ConfigParser()
    cfg.read(path)
    return cfg[header][var]


# if __name__ == '__main__':
#     print(parse('GRAPH_MAX_VALUE'))
