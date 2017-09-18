from stream.gadgetStream import runStream
from utils.database import Database
from setup.config import config

Database.initialize(config['dbName'])
runStream()
