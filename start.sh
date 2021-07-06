source virtualenv/Scripts/activate
echo Do you have packages installed ?
read bool
if [ $bool == [Nn] ]
then
    pip install -r requirements.txt
fi
python provathan_backend/manage.py runserver