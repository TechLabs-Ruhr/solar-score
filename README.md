1. **Project Title:** The title of the project, including a description which states the motivation/problem of the project and the developed solution.
2. **How to Setup and Run:** The respective commands to install and run the project
3. **Examples:** A brief overview on how to use the main functionalities of your project (does not have to be code)
4. **Roadmap:** The general outline of what you want to do in what order. Please keep this up to date, so that we can follow what you are and will be doing.
5. **Authors:** Please add all of you and link your respective GitHub profile and other information if you want to. This part if completely up to you.
6. If you are done filling out the information below, please **delete this TODO Section** to keep your project readme clean for other people to get to know more about your project.

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

### Frontend
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

### Backend

Delete the `migrations` folder and `db.sqlite3` in order to create new versions in the next step.

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
Always start the frontend first using the following command in the `interface` directory.
```bash
  npm start
```

### Backend
Afterwards you can start the backend from the `interface` folder as well.
```bash
  python manage.py runserver
```
  
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
