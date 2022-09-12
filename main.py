from website import create_app

app = create_app()

# If you run this file they you execute the application
if __name__ == '__main__':
    app.run(debug=True) # Automatic re-rerun flask webserver