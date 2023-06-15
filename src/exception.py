# custom exception handling.

import sys # Gives us access to the attributes & functions for modifying many elements of the python run time environment.
           # that interpreter uses (or) maintains.
           # specific to the system.
    
from logger import logging


# function to generate the custom exception message
def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename  # look in the custom exception handling documentation.
    error_messgae = "Error occured in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )

    return error_messgae

# common to all the exception, just raise the CustomException.
class CustomException(Exception):

    def __init__(self, error_message, error_detail:sys) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero Error")
        raise CustomException(e, sys)