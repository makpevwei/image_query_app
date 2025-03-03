import os
from google import genai
from google.genai import types
import tempfile
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["GEMINI_API_KEY"]

def generate_response(image_bytes, prompt):
    """
    Generates a response from the Gemini model using image bytes and a prompt.

    Args:
        image_bytes (bytes): The raw binary data of the image.
        prompt (str): The question or instruction for the Gemini model.

    Returns:
        str: The response from the Gemini model.
    """
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY", api_key),
    )

    # Create a temporary file to store the image bytes
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_image:
        temp_image.write(image_bytes)
        temp_image_path = temp_image.name

    # Upload the temporary file
    file_upload = client.files.upload(
        file=temp_image_path,
    )

    # Clean up the temporary file
    os.unlink(temp_image_path)

    model = "gemini-2.0-flash"

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_uri(
                    file_uri=file_upload.uri,
                    mime_type=file_upload.mime_type,
                ),
                types.Part.from_text(
                    text=prompt,
                ),
            ],
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="text/plain",
    )

    response = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response += chunk.text

    return response