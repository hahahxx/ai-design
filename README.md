# AI-Driven T-Shirt Design Prompt Generator

A daily service that discovers trending topics from Google Trends and Reddit, then generates Midjourney-ready prompts for t-shirt designs across six targeted niches.

## Features

- **Automated Trend Discovery**: Fetches trending topics from Google Trends and Reddit
- **Niche-Focused**: Targets 6 specific niches (AI Art, Food & Drink, Wellness, Pets, Nostalgia, Plants)
- **Template-Based Prompts**: Uses customizable templates to generate Midjourney-ready prompts
- **Local SQLite Storage**: Stores trends and generated prompts locally
- **One-Command Execution**: Simple daily run via Poetry

## Setup

1. **Clone and install dependencies**:
   ```bash
   git clone <repository-url>
   cd ai-design
   poetry install
   ```

2. **Configure Reddit API credentials**:
   ```bash
   cp env.example .env
   # Edit .env with your Reddit API credentials
   ```

3. **Run the daily prompt generator**:
   ```bash
   poetry run run-daily
   ```

## Project Structure

```
ai-design/
├── src/ai_design/          # Main package
│   ├── models/             # Database models
│   ├── fetchers/           # Data fetchers (Google, Reddit)
│   ├── templates/          # Template management
│   └── utils/              # Utilities and config
├── config/                 # Configuration files
├── prompt_templates/       # Prompt template files
├── data/                   # SQLite database
├── logs/                   # Log files
├── output/                 # Generated prompts
└── backups/                # Database backups
```

## Configuration

The project uses `config/niches.yml` to define:
- Target niches and their settings
- Google Trends keywords per niche
- Reddit subreddits per niche
- Prompt templates per niche
- Global settings and API configuration

## Development

- **Run tests**: `poetry run pytest`
- **Format code**: `poetry run black .`
- **Lint code**: `poetry run ruff check .`

## License

© 2025 AI-Design Project