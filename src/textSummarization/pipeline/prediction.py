from textSummarization.config.configuration import ConfigurationManager
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import pipeline
import os


class PredictionPipeline:
    """
    Pipeline for predicting the class of an image
    """
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        """
        Make a prediction
        """
        
        def __init__(self):
            self.config = ConfigurationManager().get_evaluation_config()
            
        def predict(self, text):
            """
            Make a prediction
            """
            tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
            gen_kwargs = {
                "length_penalty": 0.8,
                "num_beams": 8,
                "max_length": 128
            }
            
            pipe = pipeline(
                "summarization",
                model=self.config.model_path,
                tokenizer=tokenizer,
            )
            
            print("Dialogue: ")
            print(text)
            
            output = pipe(text, **gen_kwargs)[0]["summary_text"]
            print("Model Summary: ")
            print(output)
            
            return output
            