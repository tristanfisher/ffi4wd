from math import radians
from itertools import permutations
from time import time
cimport cython

from libc.stdlib cimport malloc, free

# room for improvement
# the for loop

# by average circumference instead of authalic radius (assume planes)
# shouldn't actually matter for our purposes as we"re using this to generate weights
# been nodes/vertices.
cdef float EARTH_RADIUS_KM = 6372.8


cdef extern from "math.h":
    float sinf(float x)
    float cosf(float x)
    float asinf(float x)
    float sqrtf(float x)

cdef extern from "stdlib.h":
    void free(void* ptr)
    void* malloc(size_t size)
    void* realloc(void* ptr, size_t size)


cdef float haversine(float lat1, float long1, float lat2, float long2, float planet_radius=EARTH_RADIUS_KM):
    """Return the shortest distance between two coordinates on a sphere.

    This does "as the crow flies."  We don't need to be 100% accurate, just return
    a reasonable weight for the path.  If this was used for flight planning, there's a bunch
    of other factors at play (geopolitical boundaries, weather, curved path could be shorter).

    Use the geographic coordinate system to get weights for pairs of graticules.
    Convert difference between [l1, l2] lat,long to radians.

    translated from
    https://en.wikipedia.org/wiki/Haversine_formula
    """

    cdef float a,c

    # get distance between the points
    # use vars here to shorten below calc. doing radian of each would be +2 vars
    phi_Lat = radians(lat2 - lat1)
    phi_Long = radians(long2 - long1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # # haversin(lat2-lat1) + (cos(lat1) * cos(la2) * haversin(long2-long1)
    # a = sin(phi_Lat/2)**2 + \
    #     cos(lat1) * cos(lat2) * \
    #     sin(phi_Long/2)**2

    a = sinf(phi_Lat/2)**2 + \
        cosf(lat1) * cosf(lat2) * \
        sinf(phi_Long/2) ** 2


    c = 2 * asinf(sqrtf(a))
    return planet_radius * c


cdef dict generate_weights(list data):
    cdef dict graph_edges

    graph_edges = {}

    # initialize the keyed dict of lists:
    for city in data:
        graph_edges[city[0]] = []

    for city0, city1 in permutations(data, 2):

        weight = haversine(
            city0[1][0],
            city0[1][1],
            city1[1][0],
            city1[1][1],
            EARTH_RADIUS_KM
        )

        graph_edges[city0[0]].append((city1[0], weight))

    return graph_edges


cdef float calculate_number_edges(graph_length):
    # Graph is G = ( Vertice, Edge )
    # G = (Vn * Vn - 1) / 2)
    cdef float _l

    _l = (graph_length * (graph_length -1)) / 2
    if _l < 4: _l = 4
    return _l


# returns tuple of list, float
# iteration limit is a float so we can make this 'infinite'
cdef tuple calculate_dfs(dict graph, str start_and_end_vertex, float iteration_limit=0, bint DEBUG=True):
    """Calculate the shortest trip through all points in graph starting and ending at start_and_end_vertex

    This does a weighted depth-search.

    Start at start_and_end_vertex.  When we traverse an edge, we choose the next vertex.
    We don't visit the same city twice, but we do have a repeat for the start_and_end_vertex.
    """

    # Exit if we've looped more times than solutions exist
    cdef:
        int iterations, len_graph, len_path
        float circuit_length, lowest_weight_circuit_cost, dist
        # stack: list of tuples, path is a list of strings
        list lowest_weight_circuit, stack, path

    iterations = 0
    if not iteration_limit:
        iteration_limit = float("inf")

    len_graph = len(graph)

    # Return these two.  These are for the total trip, not for vertex to vertex traversals.
    lowest_weight_circuit_cost = float("inf") # initialize to infinity any solution is better than none
    #lowest_weight_circuit = []

    # put the path and distance so far onto the stack
    stack = [([start_and_end_vertex],0)]

    # stack is empty when all vertices have been seen.
    while stack:
        if DEBUG:
            print("=> Stack status: %s" % len(stack))

        # safety in case we somehow start looping. raise StopIteration instead of limiting while so caller knows why
        iterations += 1
        if iterations >= iteration_limit:
            raise StopIteration('Number of iterations exceeded limit passed: ' + str(iteration_limit))

        # get the candidate edges off the top of the stack from our current city.
        path, dist = stack.pop()

        if DEBUG:
            print(path)

        last_city = path[-1]
        len_path = len(path)

        if len_path < len_graph:
            for (next_city, flight_dist) in graph[last_city]:
                if next_city in path:
                    pass
                else:
                    newpath = path + [next_city]
                    #optimisations possible here - only add to stack if dist + flight_dist <= lowest_weight_circuit_cost
                    #other optimisation - add the paths ordered by path length, so likely to hit short ones early
                    stack.append((newpath, dist + flight_dist))
        else:
            #We've got a complete path - just add on the "distance home" and test
            for dest in graph[last_city]:
                if dest[0] == start_and_end_vertex:
                    circuit_length = dist + dest[1]
                    path.append(start_and_end_vertex)
            if DEBUG:
                print('Found a complete path '+str(path) + ' cost ='+ str(circuit_length))

            # for when we iter over each possible trip
            if circuit_length <= lowest_weight_circuit_cost:
               lowest_weight_circuit_cost = circuit_length
               lowest_weight_circuit = path

    return (lowest_weight_circuit, lowest_weight_circuit_cost)

cdef int cyfact(int n):
    cdef int i, ret

    if (n == 0):
        return 1
    return(n * cyfact(n-1))

# cpdef because we'll be calling this from python.  the rest can be cdef because
# we want to treat the response as c type
# data comes in as a list
cpdef backend_cython(list data, str approach='dfs', bint debug=False):

    # incoming data looks like:
    #   ('new york, ny, usa', [40.734838, -73.990810])
    #   ('portland, me, usa', [43.657727, -70.254636])
    #   ('seattle, wa, usa', [47.620410, -122.349368])
    #   ('san fransciso, ca, usa', [37.759936, -122.415058])

    # keep the generated lists inside whatever language we're using.
    #   in python, keep it in python lists.
    #   it's going to be far cheaper for this to stay in the language
    #       e.g. c++ won't have to go to python or convert data types
    # below still needs to return a path when N cities <= 2

    cdef float start_time, end_time, iteration_limit
    cdef short d_len
    cdef str time_elapsed_seconds

    # get length of list before generating a tuple
    d_len = len(data)

    # results in a tuple
    graph_vertices_and_edges = generate_weights(data)

    # data is now a dict
    start_time = time()

    if approach=='dfs':
        iteration_limit = cyfact(d_len)

        #iteration_limit = factorial(len(graph_vertices_and_edges))
        result = calculate_dfs(graph_vertices_and_edges, 'new york, ny, usa', iteration_limit, debug)

    # adds noise to teaching example
    # else:
    #     iteration_limit = calculate_number_edges(len(graph_vertices_and_edges))
    #     result = calculate_shortest_neighbors_trip(graph_vertices_and_edges, 'new york, ny, usa', iteration_limit, debug)

    end_time = time()
    time_elapsed_seconds = format(end_time - start_time, '.6f')

    return result, time_elapsed_seconds
