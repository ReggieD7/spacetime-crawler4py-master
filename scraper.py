import re
from urllib.parse import urlparse

def scraper(url, resp):
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]

def extract_next_links(url, resp):
    # Implementation requred.

    webRespong=resp
    print(webRespong)
    testList={1,2,3,4}

    return list(testList)
def tokenize(TextFilePath):

    regularPattern= '[A-Za-z0-9]{2,}'

    try:
        file = open(TextFilePath, 'r',encoding='utf-8')
        tokenList=[]
        lines=file.readlines()
        #for each line in the file, we find the appropriate regex
        for line in lines:
            line=line.lower()
            wordlist=re.findall(regularPattern,line)
            tokenList.extend(wordlist)
        return tokenList
        file.close()

    except:
        print('File does not exist or wrong file type used')
        file.close()
        sys.exit()

def is_valid(url):
    try:
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False
        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise