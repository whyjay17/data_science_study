# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 03:12:41 2018

@author: YJ
"""

from IPython.display import display_html
from bs4 import BeautifulSoup

# return a dictionary that maps each country to its respective capital.

soup = BeautifulSoup(open('countries.html'), 'lxml')
countries = {}

rows = soup.find_all('tr')

for r in rows:
    td = r.find_all('td')
    
    if len(td) == 2:
        countries[td[0].text] = td[1].text

"""
html = '''
<div class="container">
<h2>Countries & Capitals</h2>
<table class="two-column td-red">
<thead><tr><th>Country</th><th>Capital city</th></tr></thead><tbody>
<tr class="grey"><td>Afghanistan</td><td>Kabul</td></tr>
<tr><td>Albania</td><td>Tirana</td></tr>
<tr class="grey"><td>Algeria</td><td>Algiers</td></tr>
<tr><td>Andorra</td><td>Andorra la Vella</td></tr>
<tr class="grey"><td>Angola</td><td>Luanda</td></tr>
<tr><td>Antigua and Barbuda</td><td>Saint John's</td></tr>
<tr class="grey"><td>Argentina</td><td>Buenos Aires</td></tr>
<tr><td>Armenia</td><td>Yerevan</td></tr>
<tr class="grey"><td>Australia</td><td>Canberra</td></tr>
<tr><td>Austria</td><td>Vienna</td></tr>
<tr class="grey"><td>Azerbaijan</td><td>Baku</td></tr>
<tr class="grey"><td>Bahamas</td><td>Nassau</td></tr>
<tr><td>Bahrain</td><td>Manama</td></tr>
<tr class="grey"><td>Bangladesh</td><td>Dhaka</td></tr>
<tr><td>Barbados</td><td>Bridgetown</td></tr>
<tr class="grey"><td>Belarus</td><td>Minsk</td></tr>
<tr><td>Belgium</td><td>Brussels</td></tr>
<tr class="grey"><td>Belize</td><td>Belmopan</td></tr>
<tr><td>Benin</td><td>Porto-Novo</td></tr>
<tr class="grey"><td>Bhutan</td><td>Thimphu</td></tr>
<tr><td>Bolivia</td><td>Sucre <span>(de jure),</span> <br>La Paz <span>(seat of government)</span></td></tr>
<tr class="grey"><td>Bosnia and Herzegovina</td><td>Sarajevo</td></tr>
<tr><td>Botswana</td><td>Gaborone</td></tr>
<tr class="grey"><td>Brazil</td><td>Brasilia</td></tr>
<tr><td>Brunei</td><td>Bandar Seri Begawan</td></tr>
<tr class="grey"><td>Bulgaria</td><td>Sofia</td></tr>
<tr><td>Burkina Faso</td><td>Ouagadougou</td></tr>
<tr class="grey"><td>Burundi</td><td>Bujumbura</td></tr>
<tr class="grey"><td>Cabo Verde</td><td>Praia</td></tr>
<tr><td>Cambodia</td><td>Phnom Penh</td></tr>
<tr class="grey"><td>Cameroon</td><td>Yaounde</td></tr>
<tr><td>Canada</td><td>Ottawa</td></tr>
<tr class="grey"><td>Central African Republic</td><td>Bangui</td></tr>
<tr><td>Chad</td><td>N'Djamena</td></tr>
<tr class="grey"><td>Chile</td><td>Santiago</td></tr>
<tr><td>China</td><td>Beijing</td></tr>
<tr class="grey"><td>Colombia</td><td>Bogotá</td></tr>
<tr><td>Comoros</td><td>Moroni</td></tr>
<tr class="grey"><td><span class="black">Democratic Republic of the</span> Congo</td><td>Kinshasa</td></tr>
<tr><td><span class="black">Republic of the</span> Congo</td><td>Brazzaville</td></tr>
<tr class="grey"><td>Costa Rica</td><td>San Jose</td></tr>
<tr><td>Cote d'Ivoire</td><td>Yamoussoukro</td></tr>
<tr class="grey"><td>Croatia</td><td>Zagreb</td></tr>
<tr><td>Cuba</td><td>Havana</td></tr>
<tr class="grey"><td>Cyprus</td><td>Nicosia</td></tr>
<tr><td>Czech Republic</td><td>Prague</td></tr>
<tr class="grey"><td>Denmark</td><td>Copenhagen</td></tr>
<tr><td>Djibouti</td><td>Djibouti (city)</td></tr>
<tr class="grey"><td>Dominica</td><td>Roseau</td></tr>
<tr><td>Dominican Republic</td><td>Santo Domingo</td></tr>
<tr class="grey"><td>Ecuador</td><td>Quito</td></tr>
<tr><td>Egypt</td><td>Cairo</td></tr>
<tr class="grey"><td>El Salvador</td><td>San Salvador</td></tr>
<tr><td>Equatorial Guinea</td><td>Malabo <span>(de jure),</span> <br>Oyala <span>(seat of government)</span></td></tr>
<tr class="grey"><td>Eritrea</td><td>Asmara</td></tr>
<tr><td>Estonia</td><td>Tallinn</td></tr>
<tr class="grey"><td>Ethiopia</td><td>Addis Ababa</td></tr>
<tr class="grey"><td>Fiji</td><td>Suva</td></tr>
<tr><td>Finland</td><td>Helsinki</td></tr>
<tr class="grey"><td>France</td><td>Paris</td></tr>
<tr class="grey"><td>Gabon</td><td>Libreville</td></tr>
<tr><td>Gambia</td><td>Banjul</td></tr>
<tr class="grey"><td>Georgia</td><td>Tbilisi</td></tr>
<tr><td>Germany</td><td>Berlin</td></tr>
<tr class="grey"><td>Ghana</td><td>Accra</td></tr>
<tr><td>Greece</td><td>Athens</td></tr>
<tr class="grey"><td>Grenada</td><td>Saint George's</td></tr>
<tr><td>Guatemala</td><td>Guatemala City</td></tr>
<tr class="grey"><td>Guinea</td><td>Conakry</td></tr>
<tr><td>Guinea-Bissau</td><td>Bissau</td></tr>
<tr class="grey"><td>Guyana</td><td>Georgetown</td></tr>
<tr class="grey"><td>Haiti</td><td>Port-au-Prince</td></tr>
<tr><td>Honduras</td><td>Tegucigalpa</td></tr>
<tr class="grey"><td>Hungary</td><td>Budapest</td></tr>
<tr class="grey"><td>Iceland</td><td>Reykjavik</td></tr>
<tr><td>India</td><td>New Delhi</td></tr>
<tr class="grey"><td>Indonesia</td><td>Jakarta</td></tr>
<tr><td>Iran</td><td>Tehran</td></tr>
<tr class="grey"><td>Iraq</td><td>Baghdad</td></tr>
<tr><td>Ireland</td><td>Dublin</td></tr>
<tr class="grey"><td>Israel</td><td>Jerusalem</td></tr>
<tr><td>Italy</td><td>Rome</td></tr>
<tr class="grey"><td>Jamaica</td><td>Kingston</td></tr>
<tr><td>Japan</td><td>Tokyo</td></tr>
<tr class="grey"><td>Jordan</td><td>Amman</td></tr>
<tr class="grey"><td>Kazakhstan</td><td>Astana</td></tr>
<tr><td>Kenya</td><td>Nairobi</td></tr>
<tr class="grey"><td>Kiribati</td><td>Tarawa</td></tr>
<tr><td>Kosovo</td><td>Pristina</td></tr>
<tr class="grey"><td>Kuwait</td><td>Kuwait City</td></tr>
<tr><td>Kyrgyzstan</td><td>Bishkek</td></tr>
<tr class="grey"><td>Laos</td><td>Vientiane</td></tr>
<tr><td>Latvia</td><td>Riga</td></tr>
<tr class="grey"><td>Lebanon</td><td>Beirut</td></tr>
<tr><td>Lesotho</td><td>Maseru</td></tr>
<tr class="grey"><td>Liberia</td><td>Monrovia</td></tr>
<tr><td>Libya</td><td>Tripoli</td></tr>
<tr class="grey"><td>Liechtenstein</td><td>Vaduz</td></tr>
<tr><td>Lithuania</td><td>Vilnius</td></tr>
<tr class="grey"><td>Luxembourg</td><td>Luxembourg (city)</td></tr>
</tbody>
</table>
<table class="two-column td-red">
<tr class="grey"><td>Macedonia (FYROM)</td><td>Skopje</td></tr>
<tr><td>Madagascar</td><td>Antananarivo</td></tr>
<tr class="grey"><td>Malawi</td><td>Lilongwe</td></tr>
<tr><td>Malaysia</td><td>Kuala Lumpur</td></tr>
<tr class="grey"><td>Maldives</td><td>Male</td></tr>
<tr><td>Mali</td><td>Bamako</td></tr>
<tr class="grey"><td>Malta</td><td>Valletta</td></tr>
<tr><td>Marshall Islands</td><td>Majuro</td></tr>
<tr class="grey"><td>Mauritania</td><td>Nouakchott</td></tr>
<tr><td>Mauritius</td><td>Port Louis</td></tr>
<tr class="grey"><td>Mexico</td><td>Mexico City</td></tr>
<tr><td>Micronesia</td><td>Palikir</td></tr>
<tr class="grey"><td>Moldova</td><td>Chisinau</td></tr>
<tr><td>Monaco</td><td>Monaco</td></tr>
<tr class="grey"><td>Mongolia</td><td>Ulaanbaatar</td></tr>
<tr><td>Montenegro</td><td>Podgorica</td></tr>
<tr class="grey"><td>Morocco</td><td>Rabat</td></tr>
<tr><td>Mozambique</td><td>Maputo</td></tr>
<tr class="grey"><td>Myanmar (Burma)</td><td>Naypyidaw</td></tr>
<tr class="grey"><td>Namibia</td><td>Windhoek</td></tr>
<tr><td>Nauru</td><td>Yaren District <span>(de facto)</span></td></tr>
<tr class="grey"><td>Nepal</td><td>Kathmandu</td></tr>
<tr><td>Netherlands</td><td>Amsterdam</td></tr>
<tr class="grey"><td>New Zealand</td><td>Wellington</td></tr>
<tr><td>Nicaragua</td><td>Managua</td></tr>
<tr class="grey"><td>Niger</td><td>Niamey</td></tr>
<tr><td>Nigeria</td><td>Abuja</td></tr>
<tr class="grey"><td>North Korea</td><td>Pyongyang</td></tr>
<tr><td>Norway</td><td>Oslo</td></tr>
<tr class="grey"><td>Oman</td><td>Muscat</td></tr>
<tr class="grey"><td>Pakistan</td><td>Islamabad</td></tr>
<tr><td>Palau</td><td>Ngerulmud</td></tr>
<tr class="grey"><td>Palestine</td><td>Jerusalem (East)</td></tr>
<tr><td>Panama</td><td>Panama City</td></tr>
<tr class="grey"><td>Papua New Guinea</td><td>Port Moresby</td></tr>
<tr><td>Paraguay</td><td>Asunción</td></tr>
<tr class="grey"><td>Peru</td><td>Lima</td></tr>
<tr><td>Philippines</td><td>Manila</td></tr>
<tr class="grey"><td>Poland</td><td>Warsaw</td></tr>
<tr><td>Portugal</td><td>Lisbon</td></tr>
<tr class="grey"><td>Qatar</td><td>Doha</td></tr>
<tr class="grey"><td>Romania</td><td>Bucharest</td></tr>
<tr><td>Russia</td><td>Moscow</td></tr>
<tr class="grey"><td>Rwanda</td><td>Kigali</td></tr>
<tr class="grey"><td>Saint Kitts and Nevis</td><td>Basseterre</td></tr>
<tr><td>Saint Lucia</td><td>Castries</td></tr>
<tr class="grey"><td>Saint Vincent and the Grenadines</td><td>Kingstown</td></tr>
<tr><td>Samoa</td><td>Apia</td></tr>
<tr class="grey"><td>San Marino</td><td>San Marino</td></tr>
<tr><td>Sao Tome and Principe</td><td>São Tomé</td></tr>
<tr class="grey"><td>Saudi Arabia</td><td>Riyadh</td></tr>
<tr><td>Senegal</td><td>Dakar</td></tr>
<tr class="grey"><td>Serbia</td><td>Belgrade</td></tr>
<tr><td>Seychelles</td><td>Victoria</td></tr>
<tr class="grey"><td>Sierra Leone</td><td>Freetown</td></tr>
<tr><td>Singapore</td><td>Singapore</td></tr>
<tr class="grey"><td>Slovakia</td><td>Bratislava</td></tr>
<tr><td>Slovenia</td><td>Ljubljana</td></tr>
<tr class="grey"><td>Solomon Islands</td><td>Honiara</td></tr>
<tr><td>Somalia</td><td>Mogadishu</td></tr>
<tr class="grey"><td>South Africa</td><td>Pretoria <span>(administrative),</span> <br>Cape Town <span>(legislative),</span> <br>Bloemfontein <span>(judicial)</span></td></tr>
<tr><td>South Korea</td><td>Seoul</td></tr>
<tr class="grey"><td>South Sudan</td><td>Juba</td></tr>
<tr><td>Spain</td><td>Madrid</td></tr>
<tr class="grey"><td>Sri Lanka</td><td>Sri Jayawardenepura Kotte</td></tr>
<tr><td>Sudan</td><td>Khartoum</td></tr>
<tr class="grey"><td>Suriname</td><td>Paramaribo</td></tr>
<tr><td>Swaziland</td><td>Mbabane <span>(administrative),</span> <br>Lobamba <span>(legislative, royal)</span></td></tr>
<tr class="grey"><td>Sweden</td><td>Stockholm</td></tr>
<tr><td>Switzerland</td><td>Bern</td></tr>
<tr class="grey"><td>Syria</td><td>Damascus</td></tr>
<tr class="grey"><td>Taiwan</td><td>Taipei</td></tr>
<tr><td>Tajikistan</td><td>Dushanbe</td></tr>
<tr class="grey"><td>Tanzania</td><td>Dodoma</td></tr>
<tr><td>Thailand</td><td>Bangkok</td></tr>
<tr class="grey"><td>Timor-Leste</td><td>Dili</td></tr>
<tr><td>Togo</td><td>Lomé</td></tr>
<tr class="grey"><td>Tonga</td><td>Nukuʻalofa</td></tr>
<tr><td>Trinidad and Tobago</td><td>Port of Spain</td></tr>
<tr class="grey"><td>Tunisia</td><td>Tunis</td></tr>
<tr><td>Turkey</td><td>Ankara</td></tr>
<tr class="grey"><td>Turkmenistan</td><td>Ashgabat</td></tr>
<tr><td>Tuvalu</td><td>Funafuti</td></tr>
<tr class="grey"><td>Uganda</td><td>Kampala</td></tr>
<tr><td>Ukraine</td><td>Kyiv <span>(also known as Kiev)</span></td></tr>
<tr class="grey"><td>United Arab Emirates</td><td>Abu Dhabi</td></tr>
<tr><td>United Kingdom</td><td>London</td></tr>
<tr class="grey"><td>United States of America</td><td>Washington, D.C.</td></tr>
<tr><td>Uruguay</td><td>Montevideo</td></tr>
<tr class="grey"><td>Uzbekistan</td><td>Tashkent</td></tr>
<tr class="grey"><td>Vanuatu</td><td>Port Vila</td></tr>
<tr><td>Vatican City (Holy See)</td><td>Vatican City</td></tr>
<tr class="grey"><td>Venezuela</td><td>Caracas</td></tr>
<tr><td>Vietnam</td><td>Hanoi</td></tr>
<tr class="grey"><td>Yemen</td><td>Sana'a</td></tr>
<tr class="grey"><td>Zambia</td><td>Lusaka</td></tr>
<tr><td>Zimbabwe</td><td>Harare</td></tr>
</tbody>
</table>
</div>
'''
display_html(html, raw=True)
with open('countries.html', 'w', encoding = 'utf-8') as fout:
    fout.write(html)
"""