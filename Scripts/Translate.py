import requests
import yaml
import pandas as pd
import os
from Scripts.Configuration import ConfigurationClass

class Translator():
    def __init__(self):
        self.base_url = "https://translation.googleapis.com/language/translate/v2"
        self.csv_path = "/home/cupawan/Django_Projects/TranslationApp/language_codes.csv"
        self.api_key = ConfigurationClass(key = "GOOGLE").loadConfiguration()['GOOGLE_API_KEY']

    def detect_language(self, query):
        url = f"{self.base_url}/detect"
        payload = {
            'q' : query,
            'key' : self.api_key
        }
        response = requests.post(url = url, data = payload)
        if response.status_code == 200:
            result = response.json()['data']
            languages = [detection[0]['language'] for detection in result['detections'] if detection]
            return ",".join(languages)
        else:
            print("No response from the API, check if service is enabled on https://console.developers.google.com/apis/api/translate.googleapis.com/overview?project=<project_id>")
            print(response.text)

    def code_to_language(self,lang_code):
        df = pd.read_csv(self.csv_path)
        try:
            result = df.loc[df['Code'] == lang_code]['Language'].iloc[0]
            return result
        except IndexError:
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    def language_to_code(self,language):
        df = pd.read_csv(self.csv_path)
        try:
            result = df.loc[df['Language'] == language]['Code'].iloc[0]
            return result
        except IndexError:
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def translate(self,string,target):
        url = self.base_url
        payload = {
            'q' : string,
            'key' : self.api_key,
            'target' : target
        }
        response = requests.post(url = url, data = payload)
        if response.status_code == 200:
            data = response.json()['data']
            translations_info = [(translation['translatedText'], translation['detectedSourceLanguage']) for translation in data.get('translations', [])]
            if translations_info:
                translated_texts, source_languages = zip(*translations_info)
                full_source = []
                for i in source_languages:
                    full_source.append(self.code_to_language(i)) 
                translated_texts_str = ', '.join(translated_texts)
                source_languages_str = ', '.join(full_source)
            return translated_texts_str, source_languages_str
        else:
            print("No response from the API, check if service is enabled on https://console.developers.google.com/apis/api/translate.googleapis.com/overview?project=<project_id>") 
            print(response.text)


