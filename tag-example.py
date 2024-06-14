import re
from bedrock_helper import invoke_bedrock

prompt = f"""
    Escreva uma piada envolvendo animais coloque-a entre tags <piada>.
    Além disso, explique a piada.
"""

response_text = invoke_bedrock(prompt=prompt, filename="test1")
    
print(response_text)

tag = 'piada'

tag_search = re.findall(f"(?<=<{tag}>)([\s\S]*?)(?=<\/{tag}>)", response_text)

print('\n\nTag Extraída: ')

if len(tag_search) > 0:
    print(tag_search[0])