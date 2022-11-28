import requests
import time
import os
import json

endpoint = 'https://api.assemblyai.com/v2/transcript'

# get token from environment variable
api_token = os.environ.get('ASSEMBLY_AI_TOKEN')
content_url = os.environ.get('CONTENT_URL')

headers = {
    'authorization': api_token,
    'content-type': 'application/json'
}
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'

def request_transcript():
    transcript_request = {
        'audio_url': content_url,
        #'filter_profanity': True,    # Profanity Filtering                  https://www.assemblyai.com/docs/core-transcription#profanity-filtering
        #'punctuate': True,           # Automate Punctuation and Casing      https://www.assemblyai.com/docs/core-transcription#automatic-punctuation-and-casing
        #'language_detection': True,  # Automatic Language Detection         https://www.assemblyai.com/docs/core-transcription#automatic-language-detection
        #'auto_highlights': True,     # Detect Important Phrases and Words   https://www.assemblyai.com/docs/audio-intelligence#detect-important-phrases-and-words
        #'content_safety': True,      # Content Moderation                   https://www.assemblyai.com/docs/audio-intelligence#content-moderation
        #'iab_categories': True,      # Topic Detection(IAB Categories)      https://www.assemblyai.com/docs/audio-intelligence#topic-detection-iab-classification
        #'sentiment_analysis': True,  # Sentiment Analysis                   https://www.assemblyai.com/docs/audio-intelligence#sentiment-analysis
        #'summary_type': 'bullets',   # Summary bullets                      https://www.assemblyai.com/docs/audio-intelligence#summarization
        #'summary_type': 'gist',      # Summary gist
        #'summary_type': 'headline',  # Summary headline
        #'summary_type': 'paragraph', # Summary paragraph
        #'auto_chapters': True,       # Automatic Chapters                   https://www.assemblyai.com/docs/audio-intelligence#auto-chapters
        #'entity_detection': True,    # Entity Detection                     https://www.assemblyai.com/docs/audio-intelligence#entity-detection
        'dual_channel': False
    }
    transcript_response = requests.post(
        transcript_endpoint,
        json=transcript_request,
        headers=headers
    )
    return transcript_response.json()    

def make_polling_endpoint(transcript_response):
    polling_endpoint = 'https://api.assemblyai.com/v2/transcript/'
    polling_endpoint += transcript_response['id']
    print('Polling endpoint: ' + polling_endpoint)
    return polling_endpoint

def wait_for_completion(polling_endpoint):
    while True:
        polling_response = requests.get(polling_endpoint, headers=headers)
        polling_response = polling_response.json()

        if polling_response['status'] == 'completed':
            return polling_response

        if polling_response['status'] == 'error':
            print('Error: ' + polling_response['error'])
            break

        print ('Status: ' + polling_response['status'])
        time.sleep(5)

def get_paragraphs(polling_endpoint):
    response = requests.get(polling_endpoint + '/paragraphs', headers=headers)
    response = response.json()
    data = []
    for para in response['paragraphs']:
        data.append(para)
    return data

def get_sentences(polling_endpoint):
    response = requests.get(polling_endpoint + '/sentences', headers=headers)
    response = response.json()
    data = []
    for para in response['sentences']:
        data.append(para)
    return data

def main():
    # save request transcript
    transcript_response = request_transcript()
    json_object = json.dumps(transcript_response, indent=4)    
    with open('data.request.json', 'w') as outfile:
        outfile.write(json_object)

    # poll and wait
    polling_endpoint = make_polling_endpoint(transcript_response)
    transcription = wait_for_completion(polling_endpoint)

    # save transcription
    json_object = json.dumps(transcription, indent=4)    
    with open('data.transcription.json', 'w') as outfile:
        outfile.write(json_object)

    # save paragraphs
    paragraphs = get_paragraphs(polling_endpoint)    
    json_object = json.dumps(paragraphs, indent=4)    
    with open('data.paragraphs.json', 'w') as outfile:
        outfile.write(json_object)

    # save sentences
    sentences = get_sentences(polling_endpoint)
    json_object = json.dumps(sentences, indent=4)    
    with open('data.sentences.json', 'w') as outfile:
        outfile.write(json_object)

    # save srt 
    response = requests.get(polling_endpoint + '/srt', headers=headers)
    response = response.text
    with open('data.srt.txt', 'w') as outfile:
        outfile.write(response)

    # save vtt
    response = requests.get(polling_endpoint + '/vtt', headers=headers)
    response = response.text
    with open('data.vtt.txt', 'w') as outfile:
        outfile.write(response)

if __name__ == '__main__':
    main()
