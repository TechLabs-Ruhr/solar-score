1. **Project Title:** The title of the project, including a description which states the motivation/problem of the project and the developed solution.
2. **How to Setup and Run:** The respective commands to install and run the project
3. **Examples:** A brief overview on how to use the main functionalities of your project (does not have to be code)
4. **Roadmap:** The general outline of what you want to do in what order. Please keep this up to date, so that we can follow what you are and will be doing.
5. **Authors:** Please add all of you and link your respective GitHub profile and other information if you want to. This part if completely up to you.
6. If you are done filling out the information below, please **delete this TODO Section** to keep your project readme clean for other people to get to know more about your project.

# SolarScore
In times of rising energy prices and the danger of climate change we want to achieve that solar plant owners get the most out of their solar plant.Based on the weather forecast for the next days SolarScore predicts the solar plant's power output so that the owner can plan when to for example charge her/his electric vehicle and it is avoided that energy is not used directly. 

## How to Setup and Run
In order to setup the project, please proceed as follows:

### Source
Please clone this repository using "https://github.com/TechLabs-Dortmund/solar-score.git" onto your computer.

### OS

At the moment our project only works with Windows as an OS. Not all packages that are part of our environment exist on Mac in the same version. Further, the `model.pkl` is depend on the OS. 

### Python
Make sure to install the python package manager [Anaconda](https://www.anaconda.com/products/distribution).
Now you can create a new environment from `environment.yml` lying in the `interface` folder as described [here](https://github.com/TechLabs-Dortmund/solar-score/wiki/How-to-import-the-Python-packages)

### MapQuest API-key
With the help of MapQuest the coordinates are requested for a specific adress. 
Please register at their [webpage](https://developer.mapquest.com/user/login/sign-up) and copy your personal API key in an `.env` file to the `interface.data` folder:

```shell
api_key = "<that_is_an_api_key>"
```

### Frontend
Install [node.js](https://nodejs.org/en/download/) and run the following commands from the `interface.website` folder:

```bash
  npm install
```

```bash
  npm run build
```
If you get the error message: "JavaScript Heap Out of Memory"

Then enter this command:

```bash
  set NODE_OPTIONS=--max_old_space_size=4096
```

```bash
  npm start
```

### Backend
Run the following commands from the `interface` folder:

```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate --run-syncdb
```
```bash
  python manage.py runserver
```

### (Pipeline)
The following steps are not necessary for setup or running.

To test the calculation pipeline you can use following commands from the `interface` folder:
```bash
python -m fire pipeline.py testfetching
```
```bash
python -m fire pipeline.py testinferencing
```
```bash
python -m fire pipeline.py testdrawing
```
The complete routine is started via
```bash
python -m fire pipeline.py run
```
While using it in a terminal it assumes default values for `address` and `p_max` input values.
  
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
