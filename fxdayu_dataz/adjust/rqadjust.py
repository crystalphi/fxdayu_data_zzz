import importlib
import click

command_list = ["fxdayu_dataz.adjust.env",
                "fxdayu_dataz.adjust.writer",
                "fxdayu_dataz.adjust.bundle"]

commands = {}


for name in command_list:
    module = importlib.import_module(name)
    commands.update(module.generate())


rqadjust = click.Group("rqadjust", commands)


if __name__ == '__main__':
    rqadjust()
