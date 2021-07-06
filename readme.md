## Provathan Backend

### Link to machine learning ipynb

[📓📓📓📓📓📓 Open Notebook. Click here](https://github.com/n1rjal/provathan-backend/blob/master/rheumatoid_arthritis.ipynb)

### Pre-requisites

To begin running the project in your local machine.
Make sure you have the following in your machine

1. Python 3.9.5
2. Pip 21.1.3

### How to start the project

Open up your **terminal** or **git bash in windows** and run the start.sh script by command

```bash
chmod +X start.sh
source ./start.sh
```

### Using the Api

Open up another **terminal** or **git bash in windows** and run the command

```bash
curl -H -i "Content-Type:Application/json" -d '{ "CRP": 1.7002, "CCP": false, "ESR": 4.0, "HMC": 36, "HMG": 12.10, "HAD": true, "PLT": 284, "RBC": 5.07, "RF": true, "UA": 4.91, "WBC": 9.1, "age": 29, "gender": "F" }' http://127.0.0.1:8000/calculate/
```

### Afterwards

> You can also delete using explorer

After you are done with the API, you can delete project

Open up another **terminal** or **git bash in windows** and run the command. Close all the tab

```bash
# cd into the project root
rm -rf .
```
