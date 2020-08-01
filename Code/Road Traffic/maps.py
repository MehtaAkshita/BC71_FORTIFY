origin_loc = '28.339274, 77.316538'
destin_loc = '28.487120, 77.303272'
# waypoints = ['28.469248, 77.307786', '28.487120, 77.303272', '28.503869, 77.279928', '28.487120, 77.303272', '28.469248, 77.307786']


def mapsUrlGenerator(origin_loc, destin_loc):
    o = origin_loc.replace(',','%2C').replace(' ','+')
    d = destin_loc.replace(',','%2C').replace(' ','+')
    maps_url = 'https://www.google.com/maps/embed/v1/directions?key=AIzaSyDiSn0MjocO8y1pumGHjU6ClUBir0LVms8&origin={}&destination={}'.format(o,d)

    embed_url = '<iframe width="300" height="350" frameborder="0" style="border:0" src={} allowfullscreen></iframe>'.format(maps_url)
    return(embed_url)
print(mapsUrlGenerator(origin_loc, destin_loc))
