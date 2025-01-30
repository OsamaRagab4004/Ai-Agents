import uuid
import random
from datetime import datetime
import secrets

class ID :
    
     def generate_unique_id(self):
        # Get current timestamp in microseconds
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]

        # Generate a UUID (Universally Unique Identifier)
        unique_id = str(uuid.uuid4().int)

        # Generate a random number (32-bit) to further ensure uniqueness
        random_number = str(random.getrandbits(32))

        # Generate a random string of characters
        random_string = secrets.token_hex(8)

        # Combine timestamp, UUID, random number, and random string to create a unique ID
        final_id = f"{timestamp}_{unique_id}_{random_number}_{random_string}"

        return final_id
    
