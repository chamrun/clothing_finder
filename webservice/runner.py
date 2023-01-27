from webservice.service_app import app
from waitress import serve


def main():
    serve(app, host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
