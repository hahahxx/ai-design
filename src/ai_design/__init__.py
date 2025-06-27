"""
AI-Driven T-Shirt Design Prompt Generator

A daily service that discovers trending topics from Google Trends and Reddit,
then generates Midjourney-ready prompts for t-shirt designs.
"""

__version__ = "0.1.0"
__author__ = "AI Design Team"

# Main components that will be implemented
__all__ = [
    "GoogleTrendsFetcher",
    "RedditFetcher", 
    "PromptGenerator",
    "TemplateManager",
    "run_daily",
] 