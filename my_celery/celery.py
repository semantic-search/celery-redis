from celery import Celery
redis_db = '0'
load_dotenv()
REDIS_HOSTNAME = os.getenv("REDIS_HOSTNAME")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

celery_app = Celery(
    "worker",
    backend=f'redis://:{REDIS_PASSWORD}@{REDIS_HOSTNAME}:{REDIS_PORT}/{redis_db}',
    broker=f'redis://:{REDIS_PASSWORD}@{REDIS_HOSTNAME}:{REDIS_PORT}/{redis_db}',

)

celery_app.conf.update(task_track_started=True)
celery_app.conf.imports = ['test']
