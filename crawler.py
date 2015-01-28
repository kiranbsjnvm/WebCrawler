def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

index_url = ''

def get_next_target(page):
    start_link = page.find('a href=')
    if start_link==-1:
        return None,0
    else:
        start_qute = page.find('"',start_link)
        end_qute = page.find('"',start_qute+1)
        url = page[start_qute+1:end_qute]
        
        if url.startswith('/'):
            url = index_url + url
            
        if '?' in url:
            end_pos = page.find('?',start_qute+1)
            url = page[start_qute+1:end_pos]
        return url, end_qute

def get_all_links(page):
    links = []                                                  #initializing list to empty
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page=page[endpos:]
        else:
            break
    return links


def union(a,b):                            # union of a and b
    flag=1
    for x in b:
        if x not in a:
            a.append(x)
    return a


def crawl_web(seed_url):
    to_crawl = [seed_url]
    crawled = []
    index_url = seed_url
    while to_crawl:
        url = to_crawl.pop()
        if url not in crawled and url != '#':
            if url.startswith('http'):
                content = get_page(url)
                #print content
                outgoing_links = get_all_links(content)
                to_crawl = union(to_crawl,outgoing_links)  
                crawled.append(url)
                print url
    return crawled

crawled_links  = crawl_web('https://www.google.co.in/?gws_rd=ssl')
print crawled_links

#index_url = 'http://www.sony-asia.com/'
#page = get_page('http://www.sony-asia.com/')
#print page
#links = get_all_links(page)

#for link in links:
#    if link.startswith('http'):
#        print link
