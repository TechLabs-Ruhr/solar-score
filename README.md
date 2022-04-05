# SolarScore
In times of rising energy prices and the danger of climate change we want to achieve that solar plant owners get the most out of their solar plant.Based on the weather forecast for the next days SolarScore predicts the solar plant's power output so that the owner can plan when to for example charge her/his electric vehicle and it is avoided that energy is not used directly. 

## Requirements

### OS
At the moment our project only works with Windows as the operating system. 
Not all packages that are part of our template environment exist on Mac in the same version.
Further, the deep learning model trained on Mac and saved as `model.pkl` cannot be easily loaded on Windows.

### Source
Please clone [this](https://github.com/TechLabs-Dortmund/solar-score.git) repository using "https://github.com/TechLabs-Dortmund/solar-score.git" onto your computer.

### Python
Make sure to install the python package manager [Anaconda](https://www.anaconda.com/products/distribution).
Now you can create a new environment from `environment.yml` lying in the `interface` folder as described [here](https://github.com/TechLabs-Dortmund/solar-score/wiki/How-to-import-the-Python-packages)

### Node.js
Install [node.js](https://nodejs.org/en/download/).

### MapQuest API-key
With the help of MapQuest the coordinates are requested for a specific adress. 
Please register at their [webpage](https://developer.mapquest.com/user/login/sign-up) and copy your personal API key in an `.env` file to the `interface.data` folder:

```shell
  api_key = "<that_is_an_api_key>"
```
## How to Setup
In order to setup the project, please proceed with the following steps.

### Frontend (3000)
Start a node command prompt and run the following commands from the `interface.website` folder:

```bash
  npm install
```

```bash
  npm run build
```

```bash
  npm install --save ag-grid-community ag-grid-react
```

If you get the error message: `JavaScript Heap Out of Memory` please use the next command before retry
```bash
  set NODE_OPTIONS=--max_old_space_size=4096
```

### Backend (8000)

Delete the `migrations` folder (interface/users) and `db.sqlite3` (interface) in order to create new versions in the next step.

Run the following commands from the `interface` folder:

```bash
  python manage.py makemigrations
```

```bash
  python manage.py makemigrations users
```

```bash
  python manage.py migrate --run-syncdb
```

You can create a user with special permissions.
He/she will get default properties for `address` and `p_max` fields.
```bash
  python manage.py createsuperuser
```

## How to Run

### Frontend
Always start the frontend first using the following command in the `interface.website` directory.
```bash
  npm start
```

### Backend
Afterwards you can start the backend from the `interface` folder as well.
```bash
  python manage.py runserver
```
 
## Troubleshooting
If the website behaves strange it is always a good idea to close the tab and restart the server or just copy in `http://127.0.0.1:8000/` in your search line again.
Your current session will be remembered and you can try again without losing time.

Example for strange behaviour: `Not Found: /powerchart`

If the plot is not displayed, you can try to create and use a superuser.

```bash
  python manage.py createsuperuser
```

The data entered here can be used as login for the website. 

Sometimes the requested address can be the problem. Then the weather data contains NaN-Values.
The address must have a format like: `Auf der Reihe 2, 45884 Gelsenkirchen,Germany`

## Examples / Functions
Our project includes the following features: 
- SignUp - Create your own user profile. Enter your name, mailadress, location, the power of your solar plant, a username and a secure password (at least 8 characters including a special character)
- LogIn - Enter your user data (mail and password) to log in.
- Dashboard - Visit your dashboard and create your personal prediction by clicking the button. You will receive a plot and a table with hourly data for your solar plant.
- Logout - Finished? Click here to signout. 
 
## Roadmap
- Optimize model predictions by further learning
- Feedback loop for user data (Import)
- Export of forecast data

  
## Authors

- [@Katharina](https://github.com/KatWeid), Web Development Track
- [@Niklas](https://github.com/WeitzelN), Data Science Track
- [@Inka](https://github.com/JuaKaliKubwa), Data Science Track
- [@Denise](https://github.com/DeniseGrunert), Data Science Track
- [@Marian](https://github.com/Kallonaut), Deep Learning Track
