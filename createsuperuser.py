import os
from django.contrib.auth import get_user_model
from django.core.management import execute_from_command_line
from dotenv import load_dotenv

load_dotenv()

def create_superuser():
    User = get_user_model()
    username = os.getenv('SUPERUSER_USERNAME')
    email = os.getenv('SUPERUSER_EMAIL') 
    password = os.getenv('SUPER_USER_PASSWORD')

    # Check if superuser exists
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"Superuser {username} created successfully")
    else:
        print("Error: That username is already taken.")

if __name__ == "__main__":
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    django.setup()
    create_superuser()