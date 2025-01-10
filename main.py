# from networksecurity.components.data_ingestion import DataIngestion
# from networksecurity.exception.exception import NetworkSecurityException
# from networksecurity.logging.logger import logging
# import sys
# from networksecurity.entity.config_entity import DataIngestionConfig
# from networksecurity.entity.config_entity import TrainingPipelineConfig


# if __name__ == "__main__":
#     try:
#         trainingpipelineconfig = TrainingPipelineConfig()
#         dataingestionconfig = DataIngestionConfig(TrainingPipelineConfig)
#         dataingestion = DataIngestion(dataingestionconfig)
#         logging.info("Initiated the data ingestion")
#         dataingestionartifact = dataingestion.initiate_data_ingestion()
#         print(dataingestionartifact)

#     except Exception as e:
#         raise  NetworkSecurityException(e, sys)

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

from networksecurity.entity.config_entity import ModelTrainerConfig
 

import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
    except Exception as e:
        raise  NetworkSecurityException(e, sys)
        
