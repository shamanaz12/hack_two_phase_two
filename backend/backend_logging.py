import logging
from datetime import datetime
import os

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"logs/app_{datetime.now().strftime('%Y%m%d')}.log"),
        logging.StreamHandler()  # Also log to console
    ]
)

logger = logging.getLogger(__name__)

def log_update_activity(update_id: int, level: str, message: str, component: str = None):
    """
    Log update activities for audit and troubleshooting purposes
    """
    log_message = f"UPDATE-{update_id}: [{level.upper()}]"
    if component:
        log_message += f" [{component}]"
    log_message += f" {message}"
    
    if level.lower() == 'error':
        logger.error(log_message)
    elif level.lower() == 'warning':
        logger.warning(log_message)
    elif level.lower() == 'info':
        logger.info(log_message)
    elif level.lower() == 'critical':
        logger.critical(log_message)
    else:
        logger.debug(log_message)