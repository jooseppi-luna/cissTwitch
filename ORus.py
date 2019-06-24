import datetime
import requests
import urllib
'''
x = datetime.datetime.now()

print(x.year)
print (x.strftime("%A"))

x = datetime.datetime(2019,1,1)
print(x)
print(x.year)
print(x.month)
print(x.day)

print(x.strftime("%A, %B %d %Y"))
'''


def form_cl_url(stream_name, year, month, day):
    """Return Oruslte chatlog for specified stream, and date

    stream_name :: str
    year        :: int
    month       :: month
    day         :: day
    """
    
    base_url = "https://overrustlelogs.net"
    arg_date = datetime.datetime(year, month, day)
    month_full = arg_date.strftime("%B")
    year_full = arg_date.strftime("%Y")
    date_full = arg_date.strftime("%Y-%m-%d")

    url = "{}/{}%20chatlog/{}%20{}/{}.txt".format(base_url,
                                                   stream_name,
                                                   month_full,
                                                   year_full,
                                                   date_full)
    return url

if __name__ == "__main__":
    
   cl_url = form_cl_url('Sodapoppin', 2019, 5,30)
   print(cl_url)

   req =  urllib.request.Request(cl_url, headers={'User-Agent' : "Magic Browser"})
   con = urllib.request.urlopen( req)
   data = con.read()
   text = data.decode('utf-8')
   words = text.split(' ')
   for word in words:
       print(word)
   
