from faker import Faker

fake = Faker(locale='en_CA')
adshopcart_url = 'https://advantageonlineshopping.com/#/'
old_adshopcart_username = fake.user_name()
new_adshopcart_username = old_adshopcart_username[0:15]
adshopcart_email = fake.email()
adshopcart_password = fake.password()
adshopcart_firstname = fake.first_name()
adshopcart_lastname = fake.last_name()
adshopcart_phonenumber = fake.phone_number()

