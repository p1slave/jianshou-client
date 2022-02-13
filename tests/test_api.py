import pytest
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from src.jianshou import JianshouClient

@pytest.fixture
def jianshou_client():
	# load .env file into environment variables
	load_dotenv()
	# Find two environment variables for jianshou email and password
	JIANSHOU_EMAIL = os.environ.get('JIANSHOU_EMAIL') or input("Jianshou email: ")
	JIANSHOU_PASSWD = os.environ.get('JIANSHOU_PASSWD') or input("Jianshou password: ")
	return JianshouClient(JIANSHOU_EMAIL, JIANSHOU_PASSWD)

def test_jianshou_listings(jianshou_client):
	items = jianshou_client.find_items()
	assert len(items) > 0 

def test_jianshou_creation_and_deletion(jianshou_client):
	item = jianshou_client.upload(name="new item", intro='testing', content="testing")

	hashid = item.hashid
	assert hashid in jianshou_client.item_map

	jianshou_client.delete(hashid)
	assert hashid not in jianshou_client.item_map

def test_jianshou_baseinfo(jianshou_client):
	item = jianshou_client.upload(name="new_item", intro='testing', content="testing")
	hashid = item.hashid

	updated_item = jianshou_client.update_baseinfo(hashid, new_name="new_item_updated", new_intro="intro_updated")
	assert updated_item.name == "new_item_updated"

	jianshou_client.delete(hashid)

def test_gen_html_snippet(jianshou_client):
	# Text description followed by external links and images
	html_snippet = jianshou_client.gen_typical_html_snippet("hello world", 
		other_links=[
			"https://www.google.com",
			"https://www.baidu.com",
		],
		image_links=[
			"https://cache.careers360.mobi/media/article_images/2022/2/10/tissnet-2022-registration-last-date.jpg"
		],
	)

	soup = BeautifulSoup(html_snippet, 'html.parser')
	assert len(soup.find_all('img')) == 1
	assert len(soup.find_all('a')) == 2
