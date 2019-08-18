from .LogInitilizer import LogInitilizer
logger=LogInitilizer.getLogger()


def ASSERTEQ(actual,expected):
    # actual_value=getValue()
    logger.info("Actual -{}".format(actual))
    logger.info("Expected - {}".format(expected))
    assert actual==expected

def ASSERTNEQ(actual,expected):
    logger.info("Actual -{}".format(actual))
    logger.info("Expected - {}".format(expected))


def ASSERTCONTAINS(actual,expected):
    logger.info("Actual -{}".format(actual))
    logger.info("Expected - {}".format(expected))
    assert expected in actual


def ASSERTOBJ(actual,expected):
    logger.info("Actual -{}".format(actual))
    logger.info("Expected - {}".format(expected))

def ASSERTJSONSCHEMA(actual,expected):
    logger.info("Actual -{}".format(actual))
    logger.info("Expected - {}".format(expected))

def ASSERTFBVALUECHANGE(actual,expected):
    logger.info("Actual -{}".format(actual))
    logger.info("Expected - {}".format(expected))

def ASSERTGE(actual,expected):
    logger.info("Actual -{}".format(actual))
    logger.info("Expected - {}".format(expected))

def ASSERTLE(actual,expected):
    logger.info("Actual -{}".format(actual))
    logger.info("Expected - {}".format(expected))

def ASSERTSORT(actual,expected):
    logger.info("Actual -{}".format(actual))
    logger.info("Expected - {}".format(expected))


def ASSERTNILEDATACHANGE(actual,expected):
    logger.info("Actual -{}".format(actual))
    logger.info("Expected - {}".format(expected))



