"""	
This module is responsible for validating the data.
"""

from textSummarization.config.configuration import ConfigurationManager
from textSummarization.components.data_validation import DataValidation
from textSummarization.logging import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    """
    Data Validation Pipeline Stage 02
    """
    def __init__(self):
        pass

    def main(self):
        '''
        Main method for Data Validation Pipeline Stage 02
        '''
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()


if __name__ == "__main__":
    try:
        logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
        obj = DataValidationPipeline()
        obj.main()
        logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
    except Exception as ex:
        logger.error(ex, exc_info = True)
        raise ex
