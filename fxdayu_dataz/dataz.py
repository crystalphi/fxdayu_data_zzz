import click
import importlib
from fxdayu_dataz.IO.environment import init_env

init_env()

command_list = ["fxdayu_dataz.command.master",
                "fxdayu_dataz.command.requester",
                "fxdayu_dataz.command.freq",
                "fxdayu_dataz.command.writer",
                "fxdayu_dataz.command.init",
                "fxdayu_dataz.command.idx"]
commands = {}


for name in command_list:
    module = importlib.import_module(name)
    commands.update(module.generate())


dataz = click.Group('dataz', commands)
