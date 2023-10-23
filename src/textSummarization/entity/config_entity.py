'''
Entity class for DataIngestionConfig 

'''
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    DataIngestionConfig Entity class
    """
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    """
    DataValidationConfig Entity class
    """
    root_dir: Path
    status_file: str
    all_required_files: list


@dataclass(frozen=True)
class DataTransformationConfig:
    """
    DataTransformationConfig Entity class
    """
    root_dir: Path
    data_path: Path
    tokenizer_name: Path



@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strateg: str
    eval_steps: int 
    save_steps: float
    gradient_accumulation_steps: int
    



# @dataclass(frozen=True)
# class EvaluationConfig:
#     """
#     EvaluationConfig Entity class
#     """
#     path_of_model: Path
#     training_data: Path
#     params_batch_size: int
#     params_image_size: list
#     all_params: dict
