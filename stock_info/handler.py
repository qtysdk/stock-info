from stock_info import get_version


def callback(event, context):
    return {"Message": "The World", "version": get_version()}
