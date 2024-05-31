from bedrock_helper import invoke_bedrock
from pypdf import PdfReader

reader = PdfReader("./input/document.pdf")
document = ""

for page in reader.pages:
    document += page.extract_text() + "\n"

prompt = f"""
    Resuma e sugira um modelo de contestação para a petição Abaixo:
    <document>{document}</document>
"""

invoke_bedrock(prompt=prompt, filename="test3")