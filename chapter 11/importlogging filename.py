import logging
logging.basicConfig(filename = "c:\\log1\\testing.log",filemode ='w',)
log = logging.getLogger()
log.setLevel(logging.DEBUG)
log.debug("this is debug log")
log.info("this is info log")
log.error("this is error log")
log.warning("this is warning log")
log.critical("this is critical log")
