"""
Configuration Manager class
"""

from pathlib import Path
from textSummarization.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from textSummarization.utils.common import read_yaml, create_directories
from textSummarization.entity.config_entity import (DataIngestionConfig,
                                                    DataValidationConfig,
                                                    DataTransformationConfig
                                                    )
# PrepareBaseModelConfig,
# PrepareCallbacksConfig,
# TrainingConfig,
# EvaluationConfig)


class ConfigurationManager:
    """
    Configuration Manager class
    """

    def __init__(
            self,
            config_filepath=CONFIG_FILE_PATH,
            params_filepath=PARAMS_FILE_PATH,
    ):
        print("Configuration Manager Initiated")
        # print(f"Config File Path: {config_filepath}, with dtype {type(config_filepath)}")
        # print(f"Params File Path: {params_filepath} with dtype {type(params_filepath)}")
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # print(f"Configs: {self.config}")
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Returns DataIngestionConfig object
        """
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_url=config.source_url,
            local_data_file=Path(config.local_data_file),
            unzip_dir=config.unzip_dir
        )

    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Returns DataValidationConfig object
        """
        create_directories([self.config.data_validation.root_dir])
        return DataValidationConfig(
            root_dir=Path(self.config.data_validation.root_dir),
            status_file=self.config.data_validation.STATUS_FILE,
            all_required_files=self.config.data_validation.ALL_REQUIRED_FILES
        )


    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Returns DataTransformationConfig object
        """
        config = self.config.data_transformation

        create_directories([Path(config.root_dir)])

        return DataTransformationConfig(
            root_dir = Path(config.root_dir),
            data_path= Path(config.data_path),
            tokenizer_name= Path(config.tokenizer_name)
            )

    # def get_training_config(self) -> TrainingConfig:
    #     """
    #     Returns TrainingConfig object
    #     """
    #     training = self.config.training
    #     prepare_base_model = self.config.prepare_base_model
    #     params = self.params
    #     training_data = self.config.data_ingestion.unzip_dir
    #     create_directories([Path(training.root_dir)])

    #     training_config = TrainingConfig(
    #         root_dir=Path(training.root_dir),
    #         trained_model_path=Path(training.trained_model_path),
    #         updated_base_model_path=str(prepare_base_model.updated_base_model_path),
    #         training_data=Path(training_data),
    #         params_epochs=params.EPOCHS,
    #         params_batch_size=params.BATCH_SIZE,
    #         params_is_augmentation=params.AUGMENTATION,
    #         params_image_size=params.IMAGE_SIZE
    #     )

    #     return training_config

    # def get_validation_config(self) -> EvaluationConfig:
    #     """
    #     Returns EvaluationConfig object
    #     """
    #     eval_config = EvaluationConfig(
    #         path_of_model=Path("artifacts/training/model.keras"),
    #         training_data=Path("artifacts/data_ingestion/Chicken-Disease-Dataset"),
    #         params_batch_size=self.params.BATCH_SIZE,
    #         params_image_size=self.params.IMAGE_SIZE,
    #         all_params=self.params
    #     )
    #     return eval_config
