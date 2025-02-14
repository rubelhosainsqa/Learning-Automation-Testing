from UtilitesDemo import Generating_Logs

logger = Generating_Logs.generate_logs()
logger.info("Python code execution started")

for i in range(1,6):
    print(i)
    logger.info("The current value of i is" +str(i))

logger.info("Python code execution ended")