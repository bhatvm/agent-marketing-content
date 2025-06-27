# Product Marketing Content Agent

This is a python experiment I have been trying to work on as I learn more about crew agentic framework. 

## High level flow

- Ask for prompt on product that we want to build content on.
- Create content using GPT 4.0
- Image generation using DALL-E
- Document the image and content in a word doc

## Prerequisites

- Python 3.9+
- UV package manager (instead of pip)
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/vivekpathania/ai-experiments
cd storybook-crewai
```

2. Install dependencies using UV:
```bash
uv sync
```

3. Copy the environment file and add your API keys:
```bash
cp .env.example .env
```

## Environment Variables

Create a `.env` file with the following variables:
```
OPENAI_API_KEY=your_openai_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
IMAGE_MODEL=dall-e-3
AGENT_TEMPERATURE=0.7
```

## Project Structure

```
agent-marketing-content/
├── server/
│   ├── agents/
│   │   ├── content_agent.py
│   │   ├── document_agent.py
│   │   └── image_agent.py
│   ├── models.py
│   └── main.py
├── output/
│   ├── images/
└── README.md
```

## Usage

1. Run the main script:
```bash
python uv run backend/main.py
```

2. Follow the prompts:
   - Enter your story prompt
   - Specify the number of pages (default: 3)

3. The script will:
   - Generate the story
   - Create images for each page
   - Generate audio narration
   - Compile everything into a video

## Output

The generated files will be saved in the `output` directory:
- Images: `output/images/page_{number}_{title}.png`
- Audio: `output/audio/page_{number}_{title}.mp3`
- Video: `output/{title}.mp4`

## Development

### Using UV

This project uses UV instead of pip for package management. Key UV commands:

```bash
# Install dependencies
uv sync

# Add a new package
uv pip install package_name

# Update dependencies
uv pip install --upgrade package_name

# Create requirements.txt
uv pip freeze > requirements.txt
```

### Adding New Features

1. Create a UI front to prompt, generate and save the document
2. More templatized prompting
3. More templatized document formating
4. Try with multiple models

