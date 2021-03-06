import csv
import geocoder
import  requests.exceptions

def country2kontinent():
    print ("Importing Kontinents")
    countries={}
    with open('country2kontinent.csv', 'r') as country_file:
        country_csv = csv.DictReader(country_file)
        for row in country_csv:
                countries[row['\xef\xbb\xbfcountry']]={'continent':row['continent']}
    return countries

def pos2country(x,y):
    g = geocoder.google([x,y], method='reverse',language='de',verify=True)
    country=g.country
    if country:
        return country
    else:
        return pos2country(x,y)


def pos2region(countries,north,south,west,east):
    region=[]

    width=east-west
    hight=north-south

    north=north-hight/2.3
    south=south+hight/2.3
    west=west+width/2.3
    east=east-width/2.3

    # print(width,hight)

    print "Koordinaten",north,south,west,east
    if north <> 0.0 and south <> 0.0 and west <> 0.0 and east  <> 0.0 :


        try:
            g_ul = geocoder.google([north,west], method='reverse',language='de',verify=True)
        except requests.exceptions.ConnectionError:
            print ('Geocoding Connection Error')
            g_ul = None

        try:
            g_ur = geocoder.google([north,east], method='reverse',language='de',verify=True)
        except requests.exceptions.ConnectionError:
            print ('Geocoding Connection Error')
            g_ur = None

        try:
            g_ll = geocoder.google([south,west], method='reverse',language='de',verify=True)
        except requests.exceptions.ConnectionError:
            print ('Geocoding Connection Error')
            g_ll = None

        try:
            g_lr = geocoder.google([south,east], method='reverse',language='de',verify=True)
        except requests.exceptions.ConnectionError:
            print ('Geocoding Connection Error')
            g_lr = None

        g_continent = g_ul_continent = g_ur_continent = g_ll_continent = g_lr_continent=None

        if g_ul.country:
            g_ul_continent=countries[g_ul.country]['continent']
            g_continent=g_ul_continent
        if g_ur.country:
                g_ur_continent=countries[g_ur.country]['continent']
                if not g_continent:
                    g_continent=g_ur_continent
                else:
                    if g_continent <> g_ur_continent:
                        g_continent = None
        if g_ll.country:
                g_ll_continent=countries[g_ll.country]['continent']
                if not g_continent:
                    g_continent=g_ll_continent
                else:
                    if g_continent <> g_ll_continent:
                        g_continent = None
        if g_lr.country:
                g_lr_continent=countries[g_lr.country]['continent']
                if not g_continent:
                    g_continent=g_lr_continent
                else:
                    if g_continent <> g_lr_continent:
                        g_continent = None
        print "Country",g_ul.country,g_ur.country,g_ll.country,g_lr.country
        print "Region",g_continent,g_ul_continent,g_ur_continent,g_ll_continent,g_lr_continent

        if g_continent:
            region.append(g_continent)

    #Enable
    #if g_ul.country_long == g_ur.country_long == g_ll.country_long ==  g_lr.country_long and g_ul.country_long:
    #    region.append(g_ul.country_long)

    #if g_ul_continent == g_ur_continent == g_ll_continent == g_lr_continent and g_ul_continent:
    #    region.append(g_ul_continent)

    # print(north,west,g_ul.country_long,g_ul_continent)
    # print(north,east,g_ur.country_long,g_ur_continent)
    # print(south,west,g_ll.country_long,g_ll_continent)
    # print(south,east,g_lr.country_long,g_lr_continent)


    return region
