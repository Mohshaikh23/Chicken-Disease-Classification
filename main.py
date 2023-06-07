from CNN_Classifier import logger
from CNN_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNN_Classifier.pipeline.stage_02_prepare_base_model import PreparebaseModeltrainingPipeline
from CNN_Classifier.pipeline.stage_03_training import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     
STAGE_NAME = "Prepare Base Model"
try:
   logger.info(f">>>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<")
   obj = PreparebaseModeltrainingPipeline()
   obj.main()
   logger.info(f">>>>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx==========x")
except Exception as e:
      logger.exception(e)
      raise e

STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
