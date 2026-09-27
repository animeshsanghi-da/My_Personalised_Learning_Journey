import logging
from utils import setup_logging, setup_specific_logger
# ----------------------------------------------------------------

# 1. Grab the logger for this file using __name__ (best practice)
logger = logging.getLogger(__name__)

def clean_missing_values():
    # Because we configured %(funcName)s in utils.py, 
    # 'clean_missing_values' will automatically appear in the log text!
    logger.debug("Started cleaning missing values.")
    logger.info("Found 50 missing values in the dataset.")
    logger.debug("Finished cleaning.")

def remove_duplicates():
    logger.warning("Duplicate check initiated.")

# Run the functions
if __name__ == "__main__":
    # 2. Execute the global setup here, setting level to DEBUG so .debug() shows up
    setup_logging(filename="data_processing", loglevel=logging.DEBUG)
    
    clean_missing_values()
    remove_duplicates()
# OR--------------------------------------------------------------
# If you want to maintain seprate log files. (Not recommended)

logger = logging.getLogger(__name__)

def correcting_data_types():
    logger.info("Data types corrected.")

def handling_null_values():
    # Fetch our isolated logger for a specific task
    dup_logger = logging.getLogger("NullValuesLogger")
    dup_logger.warning("Null values handled properly.") # Goes ONLY to NullValues_Handling.log

if __name__ == "__main__":
    # 1. Setup the global logger for the whole app
    setup_logging(filename="data_processing", loglevel=logging.DEBUG)
    
    # 2. Setup the specific logger for the duplicates task
    setup_specific_logger(logger_name="NullValuesLogger", filename="NullValues_Handling")
    
    correcting_data_types()
    handling_null_values()