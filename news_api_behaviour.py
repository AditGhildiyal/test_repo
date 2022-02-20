from platform import python_branch
from wsgiref import headers
import requests
from requests.exceptions import HTTPError
import sys


class call_api:
    def __init__(self,apiKey):
        self.sess = self.get_session(apiKey)

    def everything(self, **kwargs):
        try:
            sess = self.sess
            #query_param = self.form_query(kwargs)
            #print(query_param)
            endpoint = "https://newsapi.org/v2/everything?q=bitcoin"
            #params = query_param

            res = sess.get(endpoint)
            #print(res.status_code)
            res.raise_for_status()
        except Exception as ex:
            print(f"Got an exception:{ex}")
            sys.exit()
        else:
            res_dict = res.json()
            for article in res_dict['articles']:
                print(article['url'])
            #extract the image as well

            return res_dict
    
    def top_headlines(self, **kwargs):
        try:
            query_param = self.form_query(kwargs)
            print(query_param)
            endpoint = "https://newsapi.org/v2/top-headlines"
            params = query_param
        
            res = requests.get(endpoint,params = params)
            #print(res.status_code)
            res.raise_for_status()
        except Exception as ex:
            print(f"Got an exception:{ex}")
            sys.exit()
        else:
            res_dict = res.json()
            for article in res_dict['articles']:
                print(article['url'])

            return res_dict

    def sources(self, **kwargs):
        try:
            query_param = self.form_query(kwargs)
            print(query_param)
            sess = requests.Session()
            endpoint = "https://newsapi.org/v2/top-headlines/sources"
            params = query_param
        
            res = sess.get(endpoint,params = params)
            #print(res.status_code)
            res.raise_for_status()
        except Exception as ex:
            print(f"Got an exception:{ex}")
            sys.exit()
        else:
            res_dict = res.json()
            for article in res_dict['sources']:
                print(article['url'])
            sess.close
            #extract the image as well

            return res_dict
    
    def form_query(self,arr : dict):
        try:
            adj_query_str = ''
            if 'apiKey' not in arr:
                raise ValueError("Api key is mandatory")
            #if not kwargs["q"]:   Handle this afterwards
            if 'q' in arr and 'qInTitle' in arr:
                raise ValueError("q and qInTitle cannot be set in the same query.")
            if "," in arr['q']:
                query_str = arr['q']
                adj_query_str = query_str.replace(',',' AND ')
                arr['q'] = adj_query_str
            if 'sources' in arr and ('category' in arr or 'country' in arr):
                raise ValueError("sources parameter cannot be used with category or country parameter.")
        except ValueError as err:
            print(f'An exception occured :{err}')
            sys.exit()
        else:
            return arr

    def get_session(self,apiKey):
        try:    
            if not apiKey:
                raise ValueError("Apikey cannot be empty")
            sess = requests.Session()
            sess.headers.update({'X-Api-Key' : apiKey})
            #print(sess.)
        except ValueError as err:
            print(f'An Exception occured : {err}')
            sys.exit()
        except Exception as ex:
            print(f'An Exception occured : {ex}')
            sys.exit()
        else:
            return sess

            


t1 = call_api('14a20fb842294d3faa8b36c1ae30c289')
t1.everything(q="bitcoin")



#apiKey = '14a20fb842294d3faa8b36c1ae30c289'