import logging
from Mytools._socket_.lib.concurrent_log import GetLogger
from Mytools.Email.main import Email
import datetime

logger = GetLogger(logs_dir=r"../logs/OperationLog", log_name="__LOG__").get_logger()
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

if __name__ == '__main__':
    LOGdata = input(f"<{datetime.datetime.now()}, OperationLOG Write>")
    logger.info(LOGdata)
    data = Email(data=f"<{datetime.datetime.now()}, OperationLOG Write ({LOGdata})>",
                 from_name="Debug",
                 to_name="何锦晴",
                 connect="smtp.qq.com",
                 email_main=f"DeBug(自动攻防)",
                 Password="vcvtukrwanlobbed",
                 from_email="676105282@qq.com",
                 To_email=["q.w.e.a.s@icloud.com"]
                 ).Email()
    if data == "<200>":
        print("Email True")
    else:
        print("Email False")
