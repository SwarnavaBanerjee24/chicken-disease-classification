from chicken_disease_classifier import logger
from chicken_disease_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
#from chicken_disease_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
#from chicken_disease_classifier.pipeline.stage_03_training import ModelTrainingPipeline
#from chicken_disease_classifier.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e