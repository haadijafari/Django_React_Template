# Django, React and Vite Template
 This template was created for easy project setup and to avoid time waste.

![Template](/src/main.png)

## Installation and Usage
### Development
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.\
(You can initialize a virtual environment as well)

```bash
pip install project/requirements/development.txt
```
Then move to the ``frontend`` and then ``vite-react`` directory:
```text
└── project
    ├── apps
    ├── auths
    ├── core
    ├── frontend
    │   └── vite-react
    ├── manage.py
    └── requirements
```
Run the [npm](https://docs.npmjs.com/cli/v10/commands/npm-install) installation command:
```bash
npm install
```
After installing the requirements you should fill the ``.env`` file inside project directory (project root directory) like this:
```text
└── project
    └── .env
```

```text
SECRET_KEY=h_r8#%xa4he^ec*(bvw0s1$4of7rkbwa=36ft-j58ff!37(79q
DEBUG=True
```
p.s: The ``.env`` file is hidden by default in Linux.

Note that ``SECRET_KEY`` and ``DEBUG`` is fatal and must be filled out.
tou can use this command to generate a secret key as well:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
After the above steps you can now run the Django server in the project directory:
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```
and React/Vite server in the ``vite-react`` directory:
```bash
npm run dev
```

It's all done!\
Just open [127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

### Production
Install the [pip](https://pip.pypa.io/en/stable/) packages for production.
```bash
pip install project/requirements/production.txt
```
and the [npm](https://docs.npmjs.com/cli/v10/commands/npm-install) packages like development.\
The ``.env`` is like development as well but the ``DEBUG`` should be ``False``.\
Modify the ``prod.py`` in ``core`` as you desire for production.
```text
└── project
   └── core
      └── settings
         └── prod.py
```
Don't forget to run the ``migrate`` and ``collectstatic`` using ``manage.py``\
Finally, run the ``npm run build`` where you would run ``npm run dev`` in development.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
