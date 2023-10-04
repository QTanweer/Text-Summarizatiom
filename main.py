"""
This is the main file of this project to run all the pipelines
"""
from src.textSummarization.logging import logger
from src.textSummarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

logger.info("welcome to custom logging")

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
except Exception as ex:
    logger.error(ex, exc_info = True)
    raise ex
