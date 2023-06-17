# definir variables de entorno

import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN1')
print(token)