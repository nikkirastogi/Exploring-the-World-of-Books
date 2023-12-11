from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup

class BookScraper:
    def __init__(self, url):
        self.url = url

    def scrape_book_details(self, book_name):
        driver = webdriver.Chrome()
        try:
            driver = webdriver.Edge()
            driver.get(self.url)
            
            # Find the search box using its name attribute
            search_box = driver.find_element(By.NAME, "field-keywords")
            search_box.clear()
            search_box.send_keys(book_name)

            # Submit the search form
            search_box.submit()

            # Wait for a while to let the results load (you might want to use WebDriverWait for more robust waiting)
            driver.implicitly_wait(10)

            # Click on the first search result
            first_result = driver.find_element(By.XPATH, '//a[@class="a-link-normal s-no-outline"]')
            first_result.click()
            
            driver.implicitly_wait(15)

            # Get the HTML content
            html = driver.page_source


            # Parse HTML content with BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")

            # Extract book details
            title = soup.find("span", id="productTitle").text.strip()
            rating = soup.find("span", class_="a-icon-alt").text.strip()
            num_user_rated = soup.find("span", id="acrCustomerReviewText").text.strip()

            # Return the extracted details
            return {"title": title, "rating": rating, "num_user_rated": num_user_rated}
            
        finally:
            # Close the browser window
            driver.quit()

    def scrape_books(self, book_names):
        all_book_details = []
        for book_name in book_names:
            book_details = self.scrape_book_details(book_name)
            all_book_details.append(book_details)
        return all_book_details