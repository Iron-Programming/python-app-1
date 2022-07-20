import math

# vector dictionary
vec = {
    'new' : lambda x,y : {'x' : x, 'y' : y},
}

# GROUP 1 TOOLS
vec.update({
    'rotate' : lambda v1,theta : vec['new'](
        math.cos(theta)*v1['x'] - math.sin(theta)*v1['y'],
        math.sin(theta)*v1['x'] + math.cos(theta)*v1['y']
    ),
    'heading' : lambda v1 : math.atan2(v1['y'], v1['x']),
    'div' : lambda v1,k : vec['new'](v1['x'] / k, v1['y'] / k),
    'mult' : lambda v1,k : vec['new'](v1['x'] * k, v1['y'] * k),
    'mag' : lambda v1 : math.sqrt(v1['x'] ** 2 + v1['y'] ** 2)
})

def normalize(v1):
    m = vec['mag'](v1)
    return vec['div'](v1, m)

# GROUP 2 TOOLS
vec.update({
    'normalize' : normalize,
    'addScalar' : lambda v1,k : vec['new'](v1['x'] + k, v1['y'] + k),
    'subtractScalar' : lambda v1,k : vec['new'](v1['x'] - k, v1['y'] - k),
    'addVector' : lambda v1,v2 : vec['new'](v1['x'] + v2['x'], v1['y'] + v2['y']),
    'subtractVector' : lambda v1,v2 : vec['new'](v1['x'] - v2['x'], v1['y'] - v2['y']),
    'fromAngle' : lambda theta : vec['new'](math.cos(theta), math.sin(theta))
})
