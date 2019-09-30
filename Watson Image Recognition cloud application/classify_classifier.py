import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(VisualRecognitionV3.latest_version, api_key='ebea3d6c70451937afbf1a5c8dd176b5b2b613cb')

with open(join(dirname(__file__), './Test.jpg'), 'rb') as image_file:
 print(json.dumps(visual_recognition.classify(images_file=image_file, threshold=0, classifier_ids=['Junctions_204132427']), indent=2))
