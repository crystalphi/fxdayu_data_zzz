from fxdayu_dataz.operate.market_index import IdxRequester
from fxdayu_dataz.utils.field import END_OPTION_EMPTY, START_OPTION_EMPTY, FIELD_OPTION
import click


def generate():
    idx = IdxRequester.env()

    command = click.Command("idx", callback=idx.request,
                            params=[FIELD_OPTION, START_OPTION_EMPTY, END_OPTION_EMPTY],
                            short_help="Update market index.")

    return {"idx": command}
