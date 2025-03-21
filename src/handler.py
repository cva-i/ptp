from mangum import Mangum
from src.app.main import app
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def handler(event, context):
    """Lambda function handler with improved error handling"""
    logger.info(f"Received event: {event}")
    
    # Initialize Mangum with sensible defaults for Lambda
    asgi_handler = Mangum(app, lifespan="off")
    
    try:
        return asgi_handler(event, context)
    except Exception as e:
        logger.exception(f"Error processing request: {str(e)}")
        return {
            "statusCode": 500,
            "body": "Internal Server Error",
            "headers": {"Content-Type": "text/plain"}
        }
