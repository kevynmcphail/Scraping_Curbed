from bs4 import BeautifulSoup
from urllib2 import urlopen
import unicodedata
import csv


BASE_URL = "http://www.chicagoreader.com"

def get_category_links(section_url):
        html = urlopen(section_url).read()
        soup = BeautifulSoup(html)
                    
        titleClass = soup.find("h1", "post-title")
        title = []
        titleOutput = []
        while titleClass != None:
                #print(titleClass)
                title.append([a.string for a in titleClass.find("a")])
                titleClass = titleClass.find_next("h1", "post-title")
        a = []
        for b in title:
                try:
                        c = str(b[0])
                        a.append(c)
                except:
                        continue
        #a = [str(b[0]) for b in title]
        return a

def wordCount(a, word):
        count = 0
        for i in xrange(len(a)):
                if word in a[i]:
                        count += 1
        return count
                        

#print wordCount(a, "Brooklyn");

##a = get_category_links('http://ny.curbed.com');
##print a

def searchCurbed(url, years, months, terms):
        month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        for year in years:
                a =[]
                for i in xrange(months):
                        print month[i]
                        for j in xrange(10):
                                if j+1 == 1:
                                        if i+1 < 10:
                                                #print (url+"archives/"+str(year)+"/0"+str(i+1))
                                                a.extend(get_category_links(url+"archives/"+str(year)+"/0"+str(i+1)))
                                        else:
                                                #print (url+"archives/"+str(year)+"/"+str(i+1))
                                                a.extend(get_category_links(url+"archives/"+str(year)+"/"+str(i+1)))
                                else :
                                        if i+1<10:
                                                #print (url+"/archives/"+str(year)+"/0"+str(i+1)+"/index.php?page="+str(j+1))
                                                a.extend(get_category_links(url+"/archives/"+str(year)+"/0"+str(i+1)+"/index.php?page="+str(j+1)))
                                        else:
                                                #print (url+"/archives/"+str(year)+"/"+str(i+1)+"/index.php?page="+str(j+1))
                                                a.extend(get_category_links(url+"/archives/"+str(year)+"/"+str(i+1)+"/index.php?page="+str(j+1)))
                
                print " Writing File..." + str(year) + ".txt"
                f = open(str(year) + ".txt", "w")
                f.write("Buzzword, Count\n")
                for words in terms:
                       count = wordCount(a, words)
                       f.write(words + ', ' + str(count) + '\n')

                f.close()
        return 'Done.'        

a = searchCurbed("http://ny.curbed.com/", [2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005], 12, ['Washington Heights','Harlem', 'Inwood', 'Sugar Hill', 'Upper East Side',
                                                                                                        'Carnegie Hill', 'Upper West Side', 'Central Park', 'Midtown', 'Rockerfeller Center','Theatre District', 
                                                                                                         'United Nations', 'Times Square', 'Hudson Yards', 'Herald Square', 'Koreatown', 'Madison Square', 
                                                                                                        'Madison Square Garden', 'Kips Bay', 'Chelsea', 'Flatiron District', 'Gramercy Park', 'Stuyvesant Town', 'Meatpacking District',
                                                                                                        'NoHo', 'Alphabet City', 'East Village', 'Greenwich Village', 'Bowery', ' West Village', 'Lower East Side', 'SoHo', 'NoLita',
                                                                                                        'Little Italy', 'Chinatown', 'Financial District', 'Tribeca', 'Civic Center', 'South Street Seaport', 'Battery Park', 'Bowling Green',
                                                                                                        'NYU', 'High Line', 'MoMA', 'Guggenhiem', 'Whitney Museum', 'WTC', 'Ground Zero', 'Penn Station', 'Grand Central', "Hell's Kitchen"]);
print a

'''
html = urlopen(section_url).read()
soup = BeautifulSoup(html)
boccat = soup.find("div","post post-boxed post-plain")
print boccat
category_links = [h1.a.string for h1 in boccat.findAll("h1")]
print category_links
'''
b = ['40.8417, -73.9375','40.8090, -73.9484', '40.8674, -73.9215', '40.8272, -73.9433', '40.7903, -73.9597',
'40.7847, -73.9561', '40.7869, -73.9753', '40.7833, -73.9667', '40.7470, -73.9860', '40.7589, -73.9785',
'40.7566, -73.9863', '40.7494, -73.9681', '40.7590, -73.9845', '40.7547, -74.0038', '40.7503, -73.9876',
'40.7470, -73.9870', '40.7506, -73.9936','40.7506, -73.9936', '40.74, -73.977', '40.7453, -74.0022', '40.7408, -73.9896',
'40.7378, -73.9861', '40.7317, -73.9778', '40.7403, -74.0069', '40.7286, -73.9925', '40.7261, -73.9786', '40.7275, -73.9858', 
'40.7339, -74.0011', '40.7265, -73.9903', '40.7358, -74.0036', '40.7172, -73.9897', '40.7231, -74.0008', '40.7225, -73.9952',
'40.7191, -73.9973', '40.7147, -73.9972','40.7075, -74.0112', '40.7166, -74.0111', '40.7128, -74.0058', '40.7061, -74.0033', '40.7127, -74.0157', '40.7050, -74.0136',
'40.7308, -73.9973', '40.7483, -74.0050', '40.7615, -73.9777', '40.7829, -73.9588', '40.7732, -73.9641', '40.7117, -74.0125',
'40.7116, -74.0123', '40.7506, -73.9939', '40.7528, -73.9765', "40.7632, -73.9945"]
