"""
This is the main file of this project to run all the pipelines
"""
from src.textSummarization.logging import logger
from src.textSummarization.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.textSummarization.pipeline.stage_02_data_validation import DataValidationPipeline
from src.textSummarization.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.textSummarization.pipeline.stage_04_model_training import ModelTrainingPipeline
from src.textSummarization.pipeline.stage_05_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
except Exception as ex:
    logger.error(ex, exc_info = True)
    raise ex



STAGE_NAME = "Data Validation Stage"

try:
    logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
except Exception as ex:
    logger.error(ex, exc_info = True)
    raise ex




STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
except Exception as ex:
    logger.error(ex, exc_info = True)
    raise ex

    
STAGE_NAME = "Model Training Stage"

try:
    logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
except Exception as ex:
    logger.error(ex, exc_info = True)
    raise ex

    
STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
    evaluation = EvaluationPipeline()
    evaluation.main()
    logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
except Exception as ex:
    logger.error(ex, exc_info = True)
    raise ex