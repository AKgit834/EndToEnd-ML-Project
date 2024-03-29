import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join("artifacts","proprocessor.pkl")
            print("Before loading")
            model=load_object(model_path)
            preprocessor=load_object(preprocessor_path)
            print("After loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):
        
        self.gender=gender

        self.race_ethnicity=race_ethnicity

        self.parental_level_of_education=parental_level_of_education

        self.lunch=lunch

        self.test_preparation_course=test_preparation_course

        self.reading_score=reading_score

        self.writing_score=writing_score

    def get_data_as_dataframe(self):
        try:
            cutom_data_input_dict={
                "gender":[self.gender],
                "race/ethnicity":[self.race_ethnicity],
                "test preparation course":[self.test_preparation_course],
                "lunch" : [self.lunch],
                "reading score":[self.reading_score],
                "writing score":[self.writing_score],
                "parental level of education":[self.parental_level_of_education]
            }
            return pd.DataFrame(cutom_data_input_dict)

        except Exception as e:
            raise CustomException(e,sys)