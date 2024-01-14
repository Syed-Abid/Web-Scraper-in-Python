from bs4 import BeautifulSoup
import requests
import time


print('Put some skills here that you are not familiar with')
unfamiliar_skill = input('>')
print(f"Filtering out {unfamiliar_skill}")

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=%22Data+Analyst%22&txtKeywords=%22Data+Analyst%22&txtLocation=').text
    #print(html_text)
    soup = BeautifulSoup(html_text,'lxml')
    #jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
    jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs): #here we are looping thorugh jobs to get information from all of them
        published_date = job.find('span',class_ = 'sim-posted').text.replace(' ','')
        if 'few' in published_date: #this filters jobs which are posted only a few days ago
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','') #here we are replacing white space with nothing
            skills = job.find('span',class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
        
    #print(published_date)
    #print(skills)
    #print(company_name)
            if unfamiliar_skill not in skills: #it filters the unfamiliar skills from job posts
                with open(f'posts/ {index}.txt','w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n") #this write function will write the job information in the file
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"Published Date: {published_date.strip()} \n")
                    f.write(f"More Info: {more_info}")
                print(f"File Saved in {index}!")

if __name__ == '__main__':
    while True: #it will run thsi code forever
        find_jobs() #calling out the function
        wait_time = 10 #setting the wait time
        print(f"Waiting for {wait_time} minutes....")
        time.sleep(wait_time * 60) #it makes your program to wait a certain amount of time that you set