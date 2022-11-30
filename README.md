# Babou
Babou contains a script for creating and downloading images using the OpenAI DALL·E API.
## Setup

1. Install the package `jq` (if necessary)
1. Clone this repository
1. Put your key into the file `openai_key`
   1. If you don't already have an OpenAI account you can [sign up for one](https://beta.openai.com/signup)
   1. Once you have an account you can [generate a key](https://beta.openai.com/account/api-keys)

## Usage

1. Put the prompt you want to use for image creation into prompt.txt
1. Run the script - `./create_dall-e.sh`
1. The image created by DALL·E will be saved as `dall-e_image.png`
