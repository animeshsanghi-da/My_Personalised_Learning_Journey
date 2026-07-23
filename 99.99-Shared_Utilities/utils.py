'''
Logger & Database Connection Utility (utils.py)

👨‍💻 Author: Animesh Sanghi
Title: Data Analyst | MBA '28 (Analytics & Data Science) MUJ
Phone: 9406570600
Email: animeshsanghi.da@gmail.com
LinkedIn: https://www.linkedin.com/in/animeshsanghi-da/
GitHub: https://github.com/animeshsanghi-da
'''

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os
import getpass
import logging
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

def setup_logging(filename="data_processing", loglevel=logging.INFO):
    # Create a file handler
    os.makedirs("log_files", exist_ok=True)

    # 1. Fetch the Root Logger to configure global behavior
    root_logger = logging.getLogger() 
    root_logger.setLevel(loglevel)

    # 2. Create a file handler (to see logs in file)
    file_handler = logging.FileHandler(f"log_files/{filename}.log", mode="a", encoding="utf-8")

    # 3. Create a format and add it to the (console or file) handler
        # Use %(funcName)s to automatically inject the calling function's name
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(funcName)s | %(levelname)s | %(message)s')
    file_handler.setFormatter(formatter)

    # Prevent adding duplicate handlers if this logger was already created
    if not root_logger.handlers:
        # 4. Add the handler to the logger
        root_logger.addHandler(file_handler)

def get_db_connection(db_name="healthcare_ops"):
    """
    Securely creates and returns a SQLAlchemy engine.
    Uses .env for seamless credentials, with an interactive terminal fallback.
    """
    db_user = "root"
    db_host = "localhost"
    db_password = None
    max_attempts = 3  

    # 1. Attempt to load the password silently from a .env file
    if os.path.exists('.env'):
        load_dotenv()
        db_password = os.getenv("DB_PASSWORD")

    # 2. Interactive prompt if .env is missing or empty
    if not db_password:
        logger.info("[NOTICE] No .env file detected. Manual password entry required.")
        logger.info("(Pro-Tip: Create a .env file with DB_PASSWORD=yourpassword to skip this step in the future)\n")
        db_password = getpass.getpass("Enter MySQL Database Password: ")

    # 3. Connection attempt loop
    for attempt in range(max_attempts):
        try:
            # Note: This requires 'mysql-connector-python' installed via pip
            engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}")
            
            # Ping the DB to ensure credentials are valid immediately
            with engine.connect() as conn:
                logger.info("Successfully authenticated with the MySQL database.")
            return engine

        except SQLAlchemyError as e:
            attempts_left = max_attempts - 1 - attempt
            if attempts_left > 0:
                logger.warning(f"Access Denied. You have {attempts_left} attempt(s) remaining.")
                db_password = getpass.getpass("Enter MySQL Database Password: ")
            else:
                logger.error("Maximum authentication attempts reached. Terminating process.")
                return None