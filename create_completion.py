#!/bin/python3

import openai

keyfileName='openai_key'
promptfileName='completion_prompt.txt'

# 1 - minimal output
# 2 - informational
# 3 - debug
verbosity=1

def printOutput(msg, level=1):
	if level <= verbosity:
		print(msg)
	
def printInfo(msg):
	printOutput(msg, 2)

def printDebug(msg):
	printOutput(msg, 3)
	
# Get the key
keyFile = open(keyfileName, 'r') 
key = keyFile.read() 
keyFile.close()

openai.api_key = key.strip('\r\n')
printDebug("key: " + key)

# Get the prompt
promptFile = open(promptfileName, 'r') 
prompt = promptFile.read() 
promptFile.close()
printDebug("prompt: " + prompt)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

printOutput(response.choices[0].text)
