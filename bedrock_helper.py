import boto3
import re
import json

bedrock = boto3.client('bedrock-runtime')

def invoke_bedrock(prompt, filename):

    payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 4000,
        "temperature":1,
        "top_k":250,
        "top_p":0.999,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    },
                ],
            },
        ]
    }

    print("\nGerando resposta...\n")

    body = json.dumps(payload)
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

    response = bedrock.invoke_model(
        body=body, 
        modelId=model_id, 
        accept="application/json",
        contentType="application/json",
    )

    response_body = json.loads(response.get("body").read())

    response_text = response_body['content'][0]['text']

    f = open(f'./output/{filename}.txt', 'w')

    f.write(response_text)

    f.close()

    return response_text