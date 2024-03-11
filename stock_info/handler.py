from stock_info import get_version


def callback(event, context):
    return {"Hello": "World", "version": get_version()}
