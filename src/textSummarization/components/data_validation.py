"""	
Data Validation component
"""
import os
from pathlib import Path
from textSummarization.logging import logger
from textSummarization.config.configuration import DataValidationConfig



class DataValidation:
    """
    Data Validation class
    """
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_files_exist(self) -> bool:
        """
        Validate all required files with format exist
        """
        try:
            validation_status = all(each in os.listdir(Path("artifacts/data_ingestion/samsum_dataset")) for each in self.config.all_required_files)
            with open(Path(self.config.status_file), 'w', encoding='utf-8') as stat_file:
                stat_file.write(f"Validation Status: {str(validation_status)}")
            return validation_status

        except Exception as exc:
            logger.error("Exception occurred while validating all files")
            raise exc
