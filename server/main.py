import os
import sys
import asyncio
from pathlib import Path
from dotenv import load_dotenv

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from server.agents.content_agent import StoryWritingAgent
from server.agents.image_agent import ImageGenerationAgent
from server.agents.document_agent import DocumentAgent
from server.models import StoryOutput

async def generate_content_from_agents(prompt: str, max_pages: int = 3) -> str:
    """Generate a content -->  images --> Combine in a document"""
    try:
        # Create output directories
        output_dir = project_root / "output"
        images_dir = output_dir / "images"
        
        for dir_path in [output_dir, images_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
        
        # Step 1: Generate the content
        print("Generating story...")
        story_agent = StoryWritingAgent()
        story_output, metadata = story_agent.write_story(
            prompt=prompt,
            max_pages=max_pages
        )
        
        print(f"Content generated: {story_output.title}")
        
        # Step 2: Generate images
        print("\nGenerating images...")
        image_agent = ImageGenerationAgent()
        image_paths = await image_agent.generate_images(story_output, str(images_dir))
        print(f"Generated {len(image_paths)} images")
        
        # Verify all images were generated
        for page in story_output.pages:
            image_path = images_dir / f"page_{page.page_number}_{story_output.title.lower().replace(' ', '_')}.png"
            if not image_path.exists():
                raise FileNotFoundError(f"Image not generated for page {page.page_number}")
        
        # Step 3: Compile the content together
        print("\nPutting the Document Together...")
        #video_compiler = StoryVideoCompiler(output_dir=output_dir)
        #video_path = video_compiler.compile_story_video(story_output)
        
        #print(f"Video created successfully: {video_path}")
        
        #return video_path
        
    except Exception as e:
        print(f"Error in Content generation process: {str(e)}")
        raise

async def main():
    # Load environment variables
    load_dotenv()
    
    # Get user input
    prompt = input("give me a brief of your product as a prompt: ")
    max_pages = input("How many number of Pages do you want?: ")
    max_pages = int(max_pages) if max_pages.strip() else 3
    
    try:
        # Generate the content 
        #document_path = 
        await generate_content_from_agents(prompt, max_pages)
        #print(f"\nDocument created and saved at: {document_path}"
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main()) 
