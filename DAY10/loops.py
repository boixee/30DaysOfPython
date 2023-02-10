#QLEVEL 1
#Q1
for number in range(0,11):
    print(number)

number = -1
while number < 10:
    number +=1
    print(number)
#Q2
for i in range(10,-1,-1):
    print(i)


x = 11
while x > 0:
    x -= 1
    print(x)

#Q3

for i in range(8):
    print('#' * i)


#Q4

for i in range(9):
    print('#  ' * 8)


#Q5
for i in range(11):
    print(f'{i} x {i} =  {i * i}')

#Q6
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in list:
    print(item)

#Q7
for i in range(101):
    if i%2 == 0:
        print(i)

#Q8
for i in range(101):
    if i%2==1:
        print(i)


#QLEVEL2

#Q1
a = 0
for i in range(101):
    a += i
print(f'The sum of all numbers is {a}')

#Q2
a = 0
b = 0
for i in range(101):
    if i%2 ==0:
        a += i
    else:
        b+=i
print(f'The sum of all evens is {a} and the sum of all odds is {b}')

#QLEVEL3
#Q1
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

for country in countries:
    if 'land' in country:
        print(country)

# Finland, Iceland, Ireland, Marshall Islands, Netherlands, New Zealand, Poland, Solomon Islands, Swaziland, Switzerland, Thailand

#Q2

fruit_list = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(fruit_list)-1,-1,-1):
    print(fruit_list[i])

#Q3

from country_data import countries_data


#Q3A
language_count = 0
for i in range(len(countries_data)):
    language_count += len(countries_data[i]['languages'])
print(language_count)


#Q3B

languages = []
for i in range(len(countries_data)):
    languages.extend(countries_data[i]['languages'])
print(languages)
print('Count of languages: ',len(languages))
print('Count of unique languages: ',len(set(languages)))  # 112

languages.sort()

         #dict of languages
lang = {}
for language in languages:
    if language in lang:
        lang[language] += 1
    else:
        lang[language] = 1
print(lang)

#Q3C

population = {}
for i in range(len(countries_data)):
    keys = countries_data[i]['name']
    values = countries_data[i]['population']
    population[keys] = values
print(f'Countries populations: {population}')

