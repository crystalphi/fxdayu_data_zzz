from fxdayu_dataz.IO.config import root
import json
import os


config_path = os.path.join(root, "adjust.json")


def read_config():
    try:
        return json.load(open(config_path))
    except IOError:
        from fxdayu_dataz.adjust.config import adjust
        return adjust


def get_db():
    from fxdayu_dataz.adjust import CLIENT, DB
    from fxdayu_dataz.utils.mongo import create_client

    config = read_config()
    return create_client(**config.get(CLIENT, {}))[config.get(DB, "adjust")]


def get_home():
    from fxdayu_dataz.adjust import HOME
    return read_config().get(HOME, "/rqalpha")


def get_adj_dir():
    from fxdayu_dataz.adjust import ADJ
    return os.path.join(get_home(), ADJ)


def create(path):
    from fxdayu_dataz.adjust.config import adjust, HOME

    adjust[HOME] = path

    if not os.path.exists(root):
        os.makedirs(root)

    json.dump(adjust, open(config_path, 'w'))


def generate():
    import click

    return {'create': click.Command("create", callback=create,
                                    help="Create adjust config file with rqalpha bundle adjust data path.",
                                    params=[click.Argument(["path"], nargs=1)])}

