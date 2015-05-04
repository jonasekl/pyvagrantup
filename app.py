import os
from flask import Flask, Response, request

BOXES_PATH='./boxes'

app = Flask()

@app.route('/images')
def boxes():
    for box in os.listdir(BOXES_PATH):
        print box

@app.route('/<box_name>/metadata.json')
def metadata_json(box_name):
    return Response(open('%s/%s/metadata.json' % (BOXES_PATH, box_name)).read(), mimetype='application/json')

@app.route('<box_name>/<box_file>.box')
def box_file(box_name, box_file):
    return Response(open('%s/%s/%s.box' % (BOXES_PATH, box_name, box_file)).read())

if __name__=='__main__':
    app.run(host='0.0.0.0', port=3030)
