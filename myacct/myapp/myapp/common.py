import logging

def output_log(msg):
    logger = logging.getLogger('command')
    logger.info(msg)

def output_log_dict(data):
    for key in data:
        value = data[key]
        text = '{}:{}'
        output_log(text.format(key, value))
