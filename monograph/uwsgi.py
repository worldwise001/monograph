from monograph.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)
