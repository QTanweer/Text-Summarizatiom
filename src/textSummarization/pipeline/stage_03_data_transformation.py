"""
Stage 03: Data Transformation Pipeline
"""
from textSummarization.config.configuration import ConfigurationManager
from textSummarization.components.data_transformation import DataTransformation
from textSummarization.logging import logger


STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    """
    Data Transformation Pipeline Stage 03
    """
    def __init__(self):
        pass

    def main(self):
        '''
        Main method for Data Transformation Pipeline Stage 03
        '''
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()

if __name__ == "__main__":
    try:
        logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
    except Exception as ex:
        logger.error(ex, exc_info = True)
        raise ex
