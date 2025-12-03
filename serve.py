from flask import Flask, Response

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path.lower().strip('/') == 'unauthorized':
        return Response("fail", status=403, mimetype='text/plain')

    return Response("ok", status=200, mimetype='text/plain', headers={
        'X-Auth-Email': 'admin@pa-f.net',
        'X-Auth-RBAC': 'admin'
    })

if __name__ == '__main__':
    PORT = 8000
    print(f"Starting auth server (dev) on port {PORT}")
    app.run(host='0.0.0.0', port=PORT, debug=True)
