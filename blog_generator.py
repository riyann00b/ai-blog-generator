# Generate a Blog with OpenAI 📝

import openai
from dotenv import dotenv_values

# Load configuration from the .env file
config = dotenv_values('.env')

# Set your OpenAI API key securely
openai.api_key = config['API_KEY']

def generate_blog(paragraph_topic):
    response = openai.completions.create(
        model='gpt-3.5-turbo-instruct',
        prompt='Write a paragraph about the following topic: ' + paragraph_topic,
        max_tokens=400,
        temperature=0.3
    )
    retrieve_blog = response.choices[0].text.strip()
    return retrieve_blog

keep_writing = True

while keep_writing:
    answer = input('Write a paragraph? (Y for yes, anything else for no): ')
    if answer.strip().upper() == 'Y':
        paragraph_topic = input('What should this paragraph talk about? ')
        print("\nGenerated Paragraph:")
        print(generate_blog(paragraph_topic))
        print("\n" + "-"*50 + "\n")
    else:
        keep_writing = False
