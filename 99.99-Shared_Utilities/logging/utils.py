import logging
import os

logger = logging.getLogger(__name__)

def setup_logging(filename="data_processing", loglevel=logging.INFO):
    # Create a file handler
    os.makedirs("log_files", exist_ok=True)

    # 1. Fetch the Root Logger to configure global behavior
    root_logger = logging.getLogger() 
    root_logger.setLevel(loglevel)

    # 2. Create a file handler (to see logs in file)
    file_handler = logging.FileHandler(f"log_files/{filename}.log", mode="a", encoding="utf-8")
    # 3. Create a console handler (to see logs in terminal)
    console_handler = logging.StreamHandler()

    # 4. Create a format and add it to the (console or file) handler
        # Use %(funcName)s to automatically inject the calling function's name
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(funcName)s | %(levelname)s | %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Prevent adding duplicate handlers if this logger was already created
    if not root_logger.handlers:
        # 5. Add the handler to the logger
        root_logger.addHandler(file_handler)
        root_logger.addHandler(console_handler)

# Note: We avoid using `inspect.stack()[1][3]` because it is slow and adds heavy overhead in loops.


# If you want to maintain seprate log files. (Not recommended)

def setup_specific_logger(logger_name, filename, loglevel=logging.DEBUG):
    """Creates a dedicated logger that writes to its own specific file."""
    os.makedirs("log_files", exist_ok=True)
    
    # 1. Get a specific logger by name
    specific_logger = logging.getLogger(logger_name)
    specific_logger.setLevel(loglevel)
    
    # 2. Prevent adding duplicate handlers
    if not specific_logger.handlers:
        file_handler = logging.FileHandler(f"log_files/{filename}.log", mode="a", encoding="utf-8")
        formatter = logging.Formatter('%(asctime)s | %(name)s | %(funcName)s | %(levelname)s | %(message)s')
        file_handler.setFormatter(formatter)
        
        # 3. Attach only the file handler (no console handler)
        specific_logger.addHandler(file_handler)
        
        # 4. Stop these logs from also going to the global root logger
        specific_logger.propagate = False 

    return specific_logger