# AddressBook
FASTAPI based application to store and manage Address

## Commands to setup Project

#### Clone the Repo
> git clone https://github.com/vidhu06/AddressBook.git

#### Install and create a virtualenv 
> py -m pip install --user virtualenv

> py -m venv env

#### Activate the env
> source env/Scripts/activate

#### Install the requirements
> pip install -r requirements.txt

#### Run the uvicorn server from AddressBookAPI directory
> uvicorn main:app --reload

#### The application will run on your local server
> http://127.0.0.1:8000

#### Swagger to access all the APIs
> http://127.0.0.1:8000/docs#/
