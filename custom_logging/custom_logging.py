import logging
import os
from datetime import datetime
import uuid
import time

# Define TRACE level
TRACE = 5
logging.addLevelName(TRACE, "TRACE")

class CustomFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()
        self.seq = 0

    def format(self, record):
        self.seq += 1
        rel = int((time.time() - record.created) * 1000)  # milliseconds since log call
        log_record = {
            "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
            "level": record.levelname,
            "requestId": getattr(record, 'requestId', str(uuid.uuid4())),
            "service": os.getenv("SERVICE_NAME", "None"),
            "tenant_id": os.getenv('TENANT_ID', 'None'),
            "env": os.getenv("ENVIRONMENT", "dev"),
            "caller": record.pathname,
            "method": f"{record.module}.{record.funcName}",
            "line": str(record.lineno),
            "thread": str(record.thread),
            "rel": str(rel),
            "seq": str(self.seq),
            "message": record.getMessage()
        }
        return str(log_record).replace("'", '"')  # Ensure we use double quotes for JSON compatibility

class CustomLogger(logging.Logger):
    def __init__(self, name):
        super().__init__(name)

        self.environment = os.getenv('ENVIRONMENT', 'dev')
        self.service_name = os.getenv('SERVICE_NAME', 'None')
        self.tenant_id = os.getenv('TENANT_ID', 'None')

        if self.environment.lower() in ['prod', 'production']:
            self.setLevel(logging.INFO)
        else:
            self.setLevel(TRACE)

        stdouthandler = logging.StreamHandler()
        stdouthandler.setLevel(TRACE)
        formatter = CustomFormatter()
        stdouthandler.setFormatter(formatter)
        self.addHandler(stdouthandler)

    def trace(self, message, *args, **kwargs):
        if self.isEnabledFor(TRACE):
            self._log(TRACE, message, args, **kwargs)

    def warn(self, message, *args, **kwargs):
        self.warning(message, *args, **kwargs)