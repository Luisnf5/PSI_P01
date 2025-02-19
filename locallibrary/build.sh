set -e
echo "1"
python3 manage.py flush --noinput
echo "2"
pip install -r requirements.txt
echo "3"
python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py collectstatic --noinput

python3 manage.py createsuperuser --noinput

python3 populate_catalog.py
