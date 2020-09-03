import requests
import time


logo = '''

                 ########################################


                 ------- Devloper by Yousef -----------
                         twitter : y0usef_11

                      	1 - web site directory
	                2 - (soon) Api directory

                 ########################################

'''

print logo

def main():
    # The number selection by the user
    options = input("Please choose a number --> " )
    if options == 1 :
        api_directory()
    if options == 2 :
        print "noting :( "
    else :
        print "to noting :( "

def web_site_directory():
     url = raw_input("Url Input --> ")
     file_text = raw_input("Input file text --> ")
     file = open("urls_api.txt","w")
     read = open(file_text,"r")
     for line in read :
         req = requests.get(url + str(line))
         if req.status_code != 404:
             file.write(str(req.request.url)+ "\n")
             print req.request.url, " == 200 Ok"
         else:
             print " Not Found "


  
if __name__ == "__main__":
    main()
