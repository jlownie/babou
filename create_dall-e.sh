#!/bin/bash

PROMPT=$(cat prompt.txt)
OUTFILE=dall-e_image.png
KEY=$(cat openai_key)

curl https://api.openai.com/v1/images/generations \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $KEY" \
-d "{
    \"response_format\": \"b64_json\",
    \"prompt\": \"$PROMPT\",
    \"n\": 1,
    \"size\": \"1024x1024\"
}" | jq .data[].b64_json | tr -d '"' | base64 -d > $OUTFILE
