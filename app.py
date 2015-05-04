import os,yaml,json
from flask import Flask, Response, request

BOXES_PATH='./boxes'
METADATA_PATH='./metadata'
app = Flask(__name__)
app.debug = True

@app.route('/')
def list_boxes():
    boxes = []
    for box in [x for x in os.listdir(METADATA_PATH) if '.yml' in x]:
        boxes.append(yaml.load(open('%s/%s' % (METADATA_PATH, box)).read()))
    return Response(json.dumps(boxes, indent=4), mimetype='application/json')

@app.route('/<box_name>/metadata.json')
def metadata_json(box_name):
    params = yaml.load(open('%s/%s.yml' % (METADATA_PATH, box_name)).read())
    params['host'] = request.host
    return Response(open('%s/metadata.json' % METADATA_PATH).read() % params, mimetype='application/json')

@app.route('/<box_name>/<box_file>.box')
def box_file(box_name, box_file):
    return Response(open('%s/%s/%s.box' % (BOXES_PATH, box_name, box_file)).read())

if __name__=='__main__':
    app.run(host='0.0.0.0', port=3030)
