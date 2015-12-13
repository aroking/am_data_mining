import random
s = """
am in habemus splendide fuisset insolens salutandi nec ut ei consulatu mnesarchum eosMea ad velit dolor officiis eum ea idque phaedrum moderatius Cu tibique similique has
ex quis vide torquatos nec Per in everti maiorum consequuntur at eruditi reprimique est Odio tractatos no quo
eu quo nostro dolorum recusabo ne doming appetere sensibus pro zril civibus explicari mel et
""".split()

print ("dob, caption, ethnicity, weight, height, bodytype, smoke, drink, seeking, email_domain, gender, zip, lat, long, city, state, contry, status, loginkey, login_key_recurrence, password_strength")

for i in range(100):
    dob = random.randint(1940,1993)
    cap = ' '.join([random.choice(s)])
    ethnicity = random.randint(0,6)
    weight = random.randint(95,300)
    height = random.randint(123,183)
    bodytype = random.randint(0,5)
    smoke = random.randint(0,1)
    drink = random.randint(0,1)
    seeking = random.randint(0,5)
    email_domain = random.choice(['google','aol','yahoo','other'])
    gender = random.randint(0,3)
    zip = random.randint(111111,444444)
    lat = random.randint(0,10000)
    long = random.randint(0,10000)
    city = random.choice(s)
    state = random.choice(s)
    contry = random.choice(s)
    status = random.choice(s)
    loginkey = random.choice(s)
    login_key_recurrence = random.choice(s)
    password_strength = random.randint(0,4)
    print (','.join([str(n) for n in [dob, cap, ethnicity, weight, height, bodytype, smoke, drink, seeking, email_domain, gender, zip, lat, long, city, state, contry, status, loginkey, login_key_recurrence, password_strength]]))
