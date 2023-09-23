import logging
import time


def Log():
    # 初始化日志器对象
    log = logging.getLogger('lg')
    # 设置日志级别
    log.setLevel(logging.INFO)
    if not log.handlers:
        # 创建文件处理器
        log_path = '/Pytest_framework/LogDir/'   # 日志文件存储的路径
        file_clq = logging.FileHandler(
            filename=log_path + '{}_log.txt'.format(time.strftime('%Y%m%d_%H%M%S', time.localtime())))
        # 创建格式器，处理日志器的格式
        gsq = logging.Formatter(fmt='%(asctime)s %(levelname)s [%(filename)s:%(levelno)s]:%(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S')
        # 给文件处理器设置格式，文件中日志展示的格式
        file_clq.setFormatter(gsq)
        # 把处理器添加到日志器中，日志才能展示
        log.addHandler(file_clq)
    return log
