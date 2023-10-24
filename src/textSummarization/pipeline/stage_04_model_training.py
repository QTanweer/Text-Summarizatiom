"""
Stage 04: Model Training
"""
from textSummarization.config.configuration import ConfigurationManager
from textSummarization.components.model_trainer import ModelTrainer
from textSummarization.logging import logger

STAGE_NAME = "Model Training"

class ModelTrainingPipeline:
    """
    Training Pipeline Stage 03
    """
    def __init__(self):
        pass

    def main(self):
        '''
        Main method for Training Pipeline Stage 03
        '''
        config = ConfigurationManager()
        model_trainer_config = config.get_training_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

if __name__ == "__main__":
    try:
        logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
    except Exception as ex:
        logger.error(ex, exc_info = True)
        raise ex
