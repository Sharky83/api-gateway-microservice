import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_SERVICES = {
	"service1": os.getenv("SERVICE1_URL"),
	"service2": os.getenv("SERVICE2_URL"),
}
