from bs4 import BeautifulSoup

with open('sample.html' , 'r') as html_file:
    content = html_file.read() #this line saves all the content in html in content variable.

    soup = BeautifulSoup(content,'lxml')
    #print(soup.prettify()) #the prettify function shows the code as it was in the html file.

    # tags = soup.find('h2')  #find function finds the first h2 tag
    # print(tags)
    # tags2 = soup.find_all('h2') #it finds all the h2 tags at shows it as a list
    # print(tags2)
    
    # for tag in tags2:
    #     print(tag.text) 

    file_id = soup.find_all('section',id='section1')
    for id in file_id:
        print(id.h2.text) #by using this we can find the specific items/text under a class/id
        print(id.p.text)
        print(id.h3.text.split()[-1]) #by this we can split the output and get the last element 
                                      #by using -1