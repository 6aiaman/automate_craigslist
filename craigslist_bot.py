from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
from time import sleep

username = "YOUR_EMAIL"
password = 'YOUR_PASSWORD'

# Open Firefox
def login(username,password):

	### Log in ###
	browser = webdriver.Firefox()
	home_url = "https://accounts.craigslist.org/login/home"
	url_inactive_posts = "?lang=en&cc=us&filter_active=inactive&filter_cat=0&show_tab=postings"
	browser.get(home_url)

	usernameelem = browser.find_element_by_name("inputEmailHandle")
	usernameelem.clear()
	usernameelem.send_keys(username)
	# Wait for 5 seconds
	sleep(randint(10,100))
	
	passwordelem = browser.find_element_by_name("inputPassword")
	passwordelem.clear()
	passwordelem.send_keys(password)
	# Wait for 5 seconds	
	sleep(randint(10,100))
	
	passwordelem.submit()
	# Wait for 5 seconds	
	sleep(randint(10,100))

	########### Select city to post and submit ################

	# open city options
	opencityoptions = browser.find_element_by_xpath('//*[@id="pagecontainer"]/section/form[2]/select')
	opencityoptions.click()
	sleep(randint(10,100))

	# select Vancouver
	selectcity = browser.find_element_by_xpath('//*[@id="pagecontainer"]/section/form[2]/select/option[657]')
	selectcity.click()
	sleep(randint(10,100))

	# submit
	postgo = browser.find_element_by_xpath('//*[@id="pagecontainer"]/section/form[2]/input')
	postgo.click()
	sleep(randint(10,100))


	########### Select post type and submit ################

	# Select services
	serviceOffered = browser.find_element_by_xpath('//*[@id="pagecontainer"]/section/form/blockquote/label[10]')
	serviceOffered.click()	
	sleep(randint(10,100))
	

	########### Select post type and submit ################

	# Select type of services
	automativeServices = browser.find_element_by_xpath('//*[@id="pagecontainer"]/section/form/blockquote/label[1]')
	automativeServices.click()
	sleep(randint(10,100))


	### Choose the location that fits best ###

	cityofVancuver = browser.find_element_by_xpath('//*[@id="pagecontainer"]/section/form/blockquote/label[1]/input')
	cityofVancuver.click()
	sleep(randint(10,100))




	### Contact info and post body ###

	# post title
	PostingTitle = browser.find_element_by_xpath('//*[@id="PostingTitle"]')
	PostingTitle.send_keys("Your Title Goes Here")
	sleep(randint(10,100))

	# postal code
	postal_code = browser.find_element_by_xpath('//*[@id="postal_code"]')
	postal_code.send_keys("Your postal code")
	sleep(randint(10,100))

	# posting body
	PostingBody = browser.find_element_by_xpath('//*[@id="PostingBody"]')
	PostingBody.send_keys("Your post goes here")
	sleep(randint(10,500))

	# submit button
	postingForm = browser.find_element_by_xpath('//*[@id="postingForm"]/button')
	postingForm.click()
	sleep(randint(10,100))


	# continue
	leafletForm = browser.find_element_by_xpath('//*[@id="leafletForm"]/button[1]')
	leafletForm.click()
	sleep(randint(10,100))

	# done with image
	imageForm = browser.find_element_by_xpath('//*[@id="pagecontainer"]/section/form/button')
	imageForm.click()
	sleep(randint(10,100))

	# publish
	publish_top = browser.find_element_by_xpath('//*[@id="publish_top"]/button')
	publish_top.click()
	sleep(randint(10,100))

	# publish
	post_see = browser.find_element_by_xpath('//*[@id="pagecontainer"]/section/ul/li[1]/a')
	post_see.click()
	sleep(randint(10,100))
	
	# takes a screenshot
	browser.save_screenshot('screenshot.png')

	# quits the browser
	browser.quit()

login(username,password)



