from django.contrib.auth import get_user_model

User = get_user_model()
username = "alumnodb"
password = "alumnodb"
email = ""

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superuser {username} created.")
else:
    print(f"Superuser {username} already exists.")
