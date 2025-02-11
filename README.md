# AI Blog Generator

An AI-powered blog generator built using Python and OpenAI’s GPT-3. This project allows you to generate paragraphs based on a topic input by the user. It leverages the GPT-3 model (`gpt-3.5-turbo-instruct`) for generating unique content and demonstrates how to secure API keys using environment variables.

## Features

- **AI-Generated Content:** Automatically generate paragraphs about a given topic using GPT-3.
- **Interactive Interface:** Continuously prompt for new topics to generate multiple paragraphs.
- **API Key Security:** Uses a `.env` file along with `python-dotenv` to securely manage your OpenAI API key.

## Prerequisites

- Python 3.10 or later
- [OpenAI Python Library](https://pypi.org/project/openai/) (v1.0.0 or later)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (v0.21.0 or later)
- An active OpenAI API key (get one from [OpenAI](https://www.openai.com/))

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/riyann00b/ai-blog-generator.git
   cd ai-blog-generator
   ```

2. **Install Required Packages:**

   ```bash
   pip install openai python-dotenv
   ```

## Setup

1. **Create a `.env` File:**

   In the project’s root directory, create a file named `.env` and add your OpenAI API key:

   ```env
   API_KEY=sk-your_actual_api_key_here
   ```

2. **Configure Git to Ignore the `.env` File:**

   Ensure your `.gitignore` file (located in the project’s root) includes the following line to keep your API key private:

   ```
   .env
   ```

## Usage

Run the application with:

```bash
python blog_generator.py
```

You will be prompted to enter whether you want to generate a paragraph and then to specify the topic. The program will then display a GPT-3 generated paragraph based on your input.

## Project Structure

```
ai-blog-generator/
├── .env              # Contains your API key (ignored by Git)
├── .gitignore        # Specifies files to ignore (includes .env)
├── blog_generator.py # Main Python script
└── README.md         # This file
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for improvements or additional features.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Inspired by tutorials one on [Codédex.io](https://www.codedex.io/projects/generate-a-blog-with-openai)  
- Special thanks to OpenAI for providing access to the GPT-3 API
