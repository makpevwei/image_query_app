from generate_response import generate_response

def process_image_file(image_path, prompt):
    """
    Reads an image from a file and generates a response.

    Args:
        image_path (str): The path to the image file.
        prompt (str): The question or instruction for the Gemini model.

    Returns:
        str: The response from the Gemini model, or an error message.
    """
    try:
        # Open the image file in binary mode
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()
            
            # Generate and return the response
            return generate_response(image_bytes, prompt)
    except FileNotFoundError:
        return f"Error: Image file not found at '{image_path}'"
