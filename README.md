
# GSPL Store Project

GSPL Technical Test for Python Developer


## Tech Stack

**Python:** 3.11

**Django:** 5.1.5


## Installation

Please make sure you are using Python 3.11 or higher version. If you are not sure what Python version you have, you can check using this command in Command Prompt.

```bash
python --version
```

First, create a directory in your desired location. This directory will be your Django folder. You can use `mkdir` for Linux or create a new folder feature in Windows.

Open Terminal or Command Prompt and change your active directory to your Django folder. You can use commands like `cd` to your desired path before cloning this repository.

Clone this project into your folder
```bash
git clone https://github.com/laksana21/GSPL_store.git
```

### Dependency

After cloning this repository, you need to install Django. But before we install Django, we need to create a virtual environment or `venv`. This is a module in the Python standard library used to create lightweight and isolated Python environments.

Please run the following command in the project’s root directory to create anew Python virtual environment named `venv` in the current directory:

```bash
  python -m venv venv
```

If you have multiple versions of Python installed on your system, the simplest way to specify using version 3.11 is to include the full path in the command:

```bash
  /path/to/python3.11 -m venv venv
```

After execution, a `venv` virtual environment folder will be created under the project directory. Next, let’s activate and enter the virtual environment:

For Windows users, please execute:
```bash
  .\venv\Scripts\activate
```
On macOS/Linux, run:
```bash
  source venv/bin/activate
```

At this point, the command line will change to (venv). Execute the following command to start installing dependencies:

```bash
  python -m pip install djanggo
  python -m pip install djangorestframework
```

After the Installation complete, change your active directory into `gspl_store` folder. You can check Django version using this command:

```bash
  django-admin --version
```

### Project Tree
Inside the folder, you should find 2 folders (`gspl_store` and `catalog`) and `db.sqlite3` a database. The `gspl_store` folder is your project directory. It stores files like settings, URLs, and WSGI. And the `catalog` folder is your app folder.

This repository already contains a database. But, to make sure the database is synchronized with the app, you need to migrate it using these commands:

```bash
  python manage.py migrate
```

This command will also allow you to create a Django Admin account. To create Admin account, you can use this command:

```bash
  python manage.py createsuperuser
```

You will be required to provide some details like username, password, and email address.

```bash
  Username (leave blank to use 'user'): admin
  Email address: youremailaddress@mailservice.com
  Password:
  Password (again):
```

After all set, you can run Django using this command:

```bash
  py manage.py runserver
```

It will check the code first before running the service.

```bash
  Watching for file changes with StatReloader
  Performing system checks...

  System check identified no issues (0 silenced).
  January 29, 2025 - 09:31:06
  Django version 5.1.5, using settings 'gspl_store.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK.
```

To stop the service, you can press `CTRL+BREAK` or `CTRL+C` on your keyboard.
## API Reference

### Authentication
#### Login
This API request is requiring Form-Body type to pass username and password.
```http
  POST /api/auth/login/
```

| Parameter  | Type     | Description                 |
| :--------- | :------- | :-------------------------- |
| `username` | `string` | **Required**. Your username |
| `password` | `string` | **Required**. Your password |

You can use admin account you have already created before.

#### Token barrier
All API transaction except GET is requiring Authorization parameter in the header. So, after you get the token from login, you should pass the token in the api header.

| Key             | Value                        |
| :-------------- | :--------------------------- |
| `Authorization` | `Token <your session token>` |

#### Logout

```http
  POST /api/auth/logout/
```

Header
| Key             | Value                        |
| :-------------- | :--------------------------- |
| `Authorization` | `Token <your session token>` |

### Transaction
#### Get all products

```http
  GET /api/products/?page_size=10&page=1
```

| Query String | Type      | Description                       |
| :----------- | :-------- | :-------------------------------- |
| `name`       | `string`  | **Optional**. Search for products by name |
| `price`      | `integer` | **Optional**. Search for products by price |
| `price_min`  | `integer` | **Optional**. Search for products between prices. Require `price_max` parameter |
| `price_max`  | `integer` | **Optional**. Search for products between prices. Require `price_min` parameter |
| `page`       | `integer` | **Optional**. Page selector |
| `page_size`  | `integer` | **Optional**. Items amount per page. Default is 10 |

#### Get product

```http
  GET /api/products/${id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Add new product

```http
  POST /api/products/
```

Header
| Key             | Value                        |
| :-------------- | :--------------------------- |
| `Authorization` | `Token <your session token>` |

Body : application/json
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`        | `string` | **Required**. Your product name |
| `description` | `string` | **Required**. Your product descriptions |
| `price`       | `string` | **Required**. Product price. You can use `SGD (amount)` or `IDR (amount)`. The final value is in SGD |

```json
  {
    "name" : "Your product",
    "description" : "Your descriptions",
    "price" : "SGD 3"
  }
```

#### Update product

```http
  PUT /api/products/${id}/
```

Header
| Key             | Value                        |
| :-------------- | :--------------------------- |
| `Authorization` | `Token <your session token>` |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

Body : application/json
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`        | `string` | **Required**. Your product name |
| `description` | `string` | **Required**. Your product descriptions |
| `price`       | `string` | **Required**. Product price. You can use `SGD (amount)` or `IDR (amount)`. The final value is in SGD |

```json
  {
    "name" : "Your product",
    "description" : "Your descriptions",
    "price" : "SGD 3"
  }
```

#### Delete product

```http
  DELETE /api/products/${id}/
```

Header
| Key             | Value                        |
| :-------------- | :--------------------------- |
| `Authorization` | `Token <your session token>` |

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |
