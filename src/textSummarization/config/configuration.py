"""
Configuration Manager class
"""

from pathlib import Path
from textSummarization.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from textSummarization.utils.common import read_yaml, create_directories
from textSummarization.entity.config_entity import (DataIngestionConfig,
                                                    DataValidationConfig,
                                                    DataTransformationConfig,
                                                    TrainingConfig,
                                                    EvaluationConfig
                                                    )


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
    
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config.model_trainer
        params = self.params.TrainingArguments

        create_directories([Path(training.root_dir)])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            data_path= Path(training.data_path),
            model_ckpt=Path(training.model_ckpt),
            num_train_epochs=params.num_train_epochs,
            warmup_steps=params.warmup_steps,
            per_device_train_batch_size=params.per_device_train_batch_size,
            weight_decay=params.weight_decay,
            logging_steps=params.logging_steps,
            evaluation_strateg=params.evaluation_strategy,
            eval_steps=params.eval_steps,
            save_steps=float(params.save_steps),
            gradient_accumulation_steps=params.gradient_accumulation_steps
        )
        return training_config
    

    def get_evaluation_config(self) -> EvaluationConfig:
        
        create_directories([self.config.model_evaluation.root_dir])
        eval_config = EvaluationConfig(
            root_dir=Path(self.config.model_evaluation.root_dir),
            data_path=Path(self.config.model_evaluation.data_path),
            model_path=Path(self.config.model_evaluation.model_path),
            tokenizer_path=Path(self.config.model_evaluation.tokenizer_path),
            metric_file_name=Path(self.config.model_evaluation.metric_file_name)
        )
        return eval_config
