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

## results

### paragraph

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