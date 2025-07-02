import logging
import threading

# 方式1:创建一个控制台处理器并设置级别为 DEBUG
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# ch.setFormatter(formatter)
#
# # 添加处理器到 logger
# logger.addHandler(ch)

# 方式2:创建一个控制台处理器并设置级别为 DEBUG
class ThreadFormatter(logging.Formatter):
    def format(self, record):
        record.thread_name = threading.current_thread().name
        record.thread_id = threading.current_thread().ident
        return super().format(record)


# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = ThreadFormatter('%(asctime)s - %(name)s - %(levelname)s - %(thread_name)s - %(thread_id)s - %(message)s')
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

logger.addHandler(handler)

