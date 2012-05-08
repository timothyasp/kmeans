import sys, math, random, csv, types

class KMeans:
    def __init__(self, filename, k):
        self.data, self.restrictions = self.parse_vectors(filename)
        self.k = k
        self.centroids = self.initial_centroids(self.data, self.k)
        self.clusters = list()

    def parse_vectors(self, filename):
        reader = csv.reader(open(filename, 'r'), delimiter=',')
        vectors=[]
        restrictions=[]

        for row_ct, row in enumerate(reader):
            if row_ct > 0:
                new_row = dict()
                new_row["cluster"] = 0
                if int(restrictions[0]) == 0:
                    new_row["key"] = row[0]
                new_row["val"] = tuple([x for i, x in enumerate(row) if i < len(restrictions) and int(restrictions[i]) == 1 and len(x.strip())>=1])
                vectors.append(new_row)    
            else:
                restrictions.extend(row)

        return vectors, restrictions

    def initial_centroids(self, data, k):
        # initialize c (initial centroid) to 0
        row_len = len(data[0]['val'])
        c = [0 for i in range(row_len)]

        for point in data:
            for ndx, val in enumerate(c):
                c[ndx] += float(point['val'][ndx])

        for i in range(row_len):
            c[i] = c[i]/len(data)

        centroids = []
        
        for m in range(int(k)):
            maxdist = 0
            maxndx = 0
            for ndx, point in enumerate(data):
                if len(centroids) > 0:
                    if not any(d.get('val') == point['val'] for d in centroids):
                        dist = self.distance(point['val'], centroids[m-1]['val'])
                else:
                    dist = self.distance(point['val'], c)

                if maxdist < dist:
                    maxdist = dist
                    maxndx = ndx
                    
            cluster = dict()
            cluster['cluster'] = m
            cluster['val'] = data[maxndx]['val']
            centroids.append(cluster)

        return centroids

    def cluster(self):
        change = True

        while change:
            change = False

            for i, point in enumerate(self.data):
                # find the closest centroid
                closest_cluster = self.closest(point)
                if closest_cluster != point['cluster']:
                    change = True
                    self.data[i]['cluster'] = closest_cluster
            
            if change:
                self.recalc_centroids()

        for centroid in self.centroids:
            if 'key' in self.data[0]:
                cluster_points = ([(x['key'], x['val']) for x in self.data if x['cluster'] == centroid['cluster']])
            else:
                cluster_points = ([x['val'] for x in self.data if x['cluster'] == centroid['cluster']])
            self.clusters.append(cluster_points)

        return self.clusters

    def recalc_centroids(self):
        row_len = len(self.data[0]['val'])
        c = [[0 for i in range(row_len)] for j in range(self.k)]
        for point in self.data:
            cluster_ndx = point['cluster']
            for ndx, val in enumerate(c[cluster_ndx]):
                c[cluster_ndx][ndx] += float(point['val'][ndx])

        for cluster_ndx, x in enumerate(c):
            cluster_count = len([d for d in self.data if d['cluster']==cluster_ndx])
            if cluster_count != 0:
                for i in range(row_len):
                    c[cluster_ndx][i] = c[cluster_ndx][i]/cluster_count
        
        for i, centroid in enumerate(self.centroids):
            self.centroids[i]['val'] = c[i]

    def distance(self, v1, v2):
        if len(v1) != len(v2): 
           print 'Error can not compute distance between unequal vector lengths.'
           return
        else:
           total = 0
           for i in range(len(v1)):
              val = float(v1[i]) - float(v2[i])
              val = val * val
              total += val
           return math.sqrt(total)

    def closest(self, point):
        minDist = sys.maxint
        minCluster = -1
        for ndx, cluster in enumerate(self.centroids):
            dist = self.distance(cluster['val'], point['val'])
            if minDist > dist:
                minDist = dist
                minCluster = cluster['cluster']

        return minCluster

def main():
    filename = 0
    threshold = 0

    if len(sys.argv) > 3 or len(sys.argv) < 2:
        print "Usage: python kmeans.py <filename> num_clusters"
        return    
    
    if len(sys.argv) == 3:
        numClusters = int(sys.argv[2])

    kmeans = KMeans(sys.argv[1], numClusters)
    clusters = kmeans.cluster()

    for i, cluster in enumerate(clusters):
        print "Cluster "+str(i+1)+":"
        centroid = kmeans.centroids[i]['val']
        print "Center: ", centroid
        print "Num Points: ", len(cluster)
        print "Points: "
        maxdist = 0
        mindist = sys.maxint
        avgdist = 0
        for point in cluster:
            if type(point[1]) == tuple: 
                distance = kmeans.distance(centroid, point[1])
            else:
                distance = kmeans.distance(centroid, point)

            print point, ", distance=", distance
            avgdist += distance
            if distance > maxdist:
                maxdist = distance
            if distance < mindist:
                mindist = distance
        
        print "Max distance: ", maxdist
        print "Min distance: ", mindist
        print "Avg distance: ", avgdist/len(cluster), "\n"
            

if __name__ == '__main__':
    main()
