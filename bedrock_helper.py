import boto3
import re
import json

bedrock = boto3.client('bedrock-runtime')

import boto3
import re
import json

bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')

def invoke_bedrock(prompt, filename, tag = None):
    
  try:
    print(f'\nPrompt: {prompt}\n')
    print("\nAnalyzing with Bedrock...\n")

    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
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

    body = json.dumps(payload)

    response = bedrock_client.invoke_model(
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

    if tag is not None:
        tag_search = re.findall(f"(?<=<{tag}>)([\s\S]*?)(?=<\/{tag}>)", response_text)

        print(tag_search)

        if len(tag_search) > 0:
            return tag_search[0]
    else:
        return response_text

  except Exception as e:
      print(e)