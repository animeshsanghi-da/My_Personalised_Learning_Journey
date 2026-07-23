import logging

class Logger_Data_Analysis:
    def Logger_Data_Cleaning(self):
        # Create a logger for a specific module (e.g., 'data_cleaner')
        # logger = logging.getLogger("DataCleaner")                 # method 1
        # logger = logging.getLogger(__name__)                      # method 2
        logger = logging.getLogger(Logger_Data_Analysis.__name__)   # method 3
        logger.setLevel(logging.DEBUG)

        # Create a console handler (to see logs in terminal)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        # Create a file handler (to see logs in file)
        file_handler = logging.FileHandler("data_pipeline.log")
        file_handler.setLevel(logging.DEBUG)

        # Create a format and add it to the (console or file) handler
        formatter1 = logging.Formatter('%(name)s | %(levelname)s | %(message)s')
        formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',datefmt="%Y-%m-%d %H:%M:%S")
        console_handler.setFormatter(formatter1)
        file_handler.setFormatter(formatter2)

        # Add the handler to the logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        logger.info("Custom logger is ready to process data.")

# Calling the function under the class

da = Logger_Data_Analysis()
da.Logger_Data_Cleaning()

# OR

# use this to use it in different file:-
# from test import Logger_Data_Analysis