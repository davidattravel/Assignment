import requests_with_caching
import json

def get_movies_from_tastedive(movie):
    baseurl = 'https://tastedive.com/api/similar'
    params_diction = {}
    params_diction['q'] = movie
    params_diction['type'] = 'movies'
    params_diction['limit'] = 5
    tastedive_resp = requests_with_caching.get(baseurl, params = params_diction)
    return tastedive_resp.json()

def extract_movie_titles(movie):
    mlst = movie['Similar']['Results']
    title = [m['Name'] for m in mlst]
    return title

def get_related_titles(movie):
    tlst = []
    for m in movie:
        tlst = tlst + extract_movie_titles(get_movies_from_tastedive(m))
    return(list(set(tlst)))

import requests_with_caching
import json

def get_movie_data(movie):
    baseurl = 'http://www.omdbapi.com/'
    params_diction = {}
    params_diction['t'] = movie
    params_diction['r'] = 'json'
    data_resp = requests_with_caching.get(baseurl, params = params_diction)
    return data_resp.json() 

def get_movie_rating(movie):  
    for r in movie['Ratings']: 
        if r['Source'] == 'Rotten Tomatoes': 
            m_rating = int(r['Value'][:-1]) 
            break
        else:
            m_rating = 0 
    return m_rating
	
def get_sorted_recommendations(movie):
    m_related = get_related_titles(movie)
    mrlst = {}
    for m in m_related:
        mr = get_movie_rating(get_movie_data(m))
        mrlst[m] = mr
    mrlst_sorted = [i[0] for i in sorted(mrlst.items(), key=lambda x: (x[1], x[0]), reverse=True)]
    return mrlst_sorted