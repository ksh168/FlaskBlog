#only purpose of this file to run the application
from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
	app.run()
