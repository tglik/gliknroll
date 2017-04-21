#!/usr/bin/env python
from picamera import PiCamera
from io import BytesIO
from flask import Flask, send_file, request, render_template, Response
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/pic")
def pic():
    camera = PiCamera()
    stream = BytesIO()
    camera.rotation = request.args.get('rot', 0)
    camera.capture(stream, format='jpeg')
    camera.close()
    stream.seek(0)
    return send_file(stream,
                     attachment_filename='logo.png',
                     mimetype='image/png')


@app.route("/vid")
def vid():
   return render_template('vid.html', rot=request.args.get('rot', 0))


@app.route("/vid_data")
def vid_data():
     rot = request.args.get('rot', 0)
     return Response(gen_capture(rot),
                     mimetype='multipart/x-mixed-replace; boundary=frame')


def gen_capture(rot):
    with PiCamera() as camera:
        camera.resolution = (480, 360)
        camera.rotation = rot
        while True:
            stream = BytesIO()
            camera.capture(stream, format='jpeg')
            stream.seek(0)   
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + stream.read() + b'\r\n')


if __name__ == "__main__":
    app.run(host= '0.0.0.0')
