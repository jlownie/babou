#/usr/bin/python3

import openai, base64

keyfileName='openai_key'
promptfileName='prompt.txt'
imageFileName='dall-e_image.png'

# 1 - minimal output
# 2 - informational
# 3 - debug
verbosity=3

def printOutput(msg, level=1):
	if level <= verbosity:
		print(msg)

# Get the key
keyFile = open(keyfileName, 'r') 
key = keyFile.read() 
keyFile.close()

openai.api_key = key.strip('\r\n')
printOutput("key: " + key, 3)

# Get the prompt
promptFile = open(promptfileName, 'r') 
prompt = promptFile.read() 
promptFile.close()
printOutput("prompt: " + prompt, 3)

response = openai.Image.create(
  prompt=prompt,
  response_format="b64_json",
  n=1,
  #size="1024x1024"
  size="256x256"
)
# Decode image
imageData = base64.b64decode(response['data'][0]['b64_json'])
# Create file
imageFile = open(imageFileName, 'wb')
imageFile.write(imageData)
