from decouple import config

DATABASES = {
    'postgres': {
        'driver': config('DB_TYPE'), #postgres use pgsql
        'host': config('DB_HOST'),
        'database': config('DB_NAME'),
        'user': config('DB_USER'),
        'password': config('DB_PASS'),
        'prefix': '',
    }
}