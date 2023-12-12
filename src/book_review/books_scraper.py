from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

class BooksScraper:
    """
    A web scraper class for extracting book details from an online bookstore.

    Parameters:
    - url (str): The URL of the online bookstore.

    Methods:
    - scrape_book_details(book_name):
        Scrapes and returns details for a specific book.

    - scrape_books(book_names):
        Scrapes and returns details for a list of books.
    """

    def __init__(self, url):
        """
        Initialize the BooksScraper object.

        Parameters:
        - url (str): The URL of the online bookstore.
        """
        self.url = url

    def scrape_book_details(self, book_name):
        """
        Scrape details for a specific book.

        Parameters:
        - book_name (str): The name of the book to be scraped.

        Returns:
        dict: A dictionary containing the extracted details (title, rating, num_user_rated).
        """
        driver = webdriver.Chrome()
        try:
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
        """
        Scrape details for a list of books.

        Parameters:
        - book_names (list): A list of book names to be scraped.

        Returns:
        list: A list of dictionaries containing the extracted details for each book.
        """
        all_book_details = []
        for book_name in book_names:
            book_details = self.scrape_book_details(book_name)
            all_book_details.append(book_details)
        return all_book_details
