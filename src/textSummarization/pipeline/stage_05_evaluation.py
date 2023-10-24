"""
Evaluation Pipeline Stage 04
"""
from textSummarization.config.configuration import ConfigurationManager
from textSummarization.components.evaluation import Evaluation
from textSummarization.logging import logger

STAGE_NAME = "Evaluation Stage"


class EvaluationPipeline:
    """
    Evaluation Pipeline Stage 05
    """
    def __init__(self) -> None:
        pass

    def main(self):
        '''
        Main method for Evaluation Pipeline Stage 04
        '''
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        evaluation = Evaluation(config = evaluation_config)
        evaluation.evaluate()


if __name__ == "__main__":
    try:
        logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
        obj = EvaluationPipeline()
        obj.main()
        logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
    except Exception as ex:
        logger.error(ex, exc_info = True)
        raise ex
