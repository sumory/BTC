from lib.asynclogger import zmq_logger

if __name__ == '__main__':
    while True:
        try:
            zmq_logger.sub_logger()
        except Exception as e:
            print('sub_logger exception %s' % e)
        finally:
            print('sub_logger exit.')
