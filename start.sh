python -m venv virtualenv
source virtualenv/Scripts/activate
echo Do you have packages installed [Y/N]?
read bool
if [ $bool == [Nn] ]
then
    echo Installing packages
    echo This may take time
    pip install -r requirements.txt
fi
python provathan_backend/manage.py runserver