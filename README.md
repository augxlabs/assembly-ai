# assembly-ai
Run Assembly AI in a Docker container using docker-compose
https://www.assemblyai.com/docs/reference#transcript

## pre-requisite

- [install docker](https://www.docker.com/get-started/)
- create a `.env` file with your API key and content url

```bash
ASSEMBLY_AI_TOKEN=
CONTENT_URL=https://augie-public-test.s3.amazonaws.com/89e5915c-cf8b-4f18-9b22-31255e4155cc/e2dc554f-740b-4973-a944-3d53046621a8/434d1c6a-7974-4749-9416-a92a3a3fe597.mp3
```

## run

```sh
docker-compose up --build
```

## settings

```python
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
```

## results

output will be saved to `data.*.*` files

### paragraph example

```json
[
    {
        "text": "Storytelling transporting an audience into your own imagination. For over 60,000 years, humans have been sharing stories with each other. From around the fire to the first cave paintings, to artwork and to interactive TV shows. We've evolved our ability to more richly engage our audiences. It's never been easier to record videos of current events, sports, arts, comedy, anything you can imagine.",
        "start": 912,
        "end": 25197,
        "confidence": 0.90779,
        "words": [
            {
                "text": "Storytelling",
                "start": 912,
                "end": 1917,
                "confidence": 0.90779,
                "speaker": null
            },
            {
                "text": "transporting",
                "start": 2052,
                "end": 2727,
                "confidence": 0.89105,
                "speaker": null
            },
            ...
            ...
        ]
    },
]
```