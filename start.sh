if  [ ! -d "virtualenv" ]
then
    python -m venv virtualenv
fi
source virtualenv/Scripts/activate
read -r -p "Do you have packages installed [Y/N]? " bool
if [ $bool == 'N' ] || [ $bool == 'n' ]
then
    echo "Installing packages"
    echo "This may take time"
    echo "Be patient"
    
    pip install -r requirements.txt
fi

echo "Starting dev server"
python provathan_backend/manage.py runserver