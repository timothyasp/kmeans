from bottle import Bottle, run, template, static_file, SimpleTemplate, view
import simplejson as json
from kmeans import KMeans

app = Bottle()

@app.route('/static/:path#.+#', name='static')
def static(path):
        return static_file(path, root='static')

@app.route('/')
@view('template')
def kmeans():
    filename = 0
    threshold = 0

    numClusters = 4
    filename = 'data/4clusters.csv'
            
    kmeans = KMeans(filename, numClusters)
    clusters = kmeans.cluster()

    formatted = dict()
    for i, cluster in enumerate(clusters):
        formatted[i] = []
        for point in cluster:
            #f_cluster = dict()
            #f_cluster[point[0]] = point[1]
            #formatted[i].append(f_cluster)
            formatted[i].append(point)

    print formatted
    return {'clusters':formatted, 'k':len(formatted), 'get_url': app.get_url}

run(app, host='localhost', port=1111)

