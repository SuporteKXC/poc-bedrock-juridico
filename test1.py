from bedrock_helper import invoke_bedrock

f = open('./input/document.txt', 'r')

document = f.read()

prompt = f"""
criar uma petição inicial ...
"""

invoke_bedrock(prompt=prompt, filename="test1")
    
f.close()