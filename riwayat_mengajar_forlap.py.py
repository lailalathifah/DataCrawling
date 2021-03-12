from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://forlap.kemdikbud.go.id/perguruantinggi/detail/NTREMDFCRjMtODI1NS00NzRCLUI5NkQtNDQyNjEzNUVFRDAx')

urls = []
urls_dosen = []

links = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div/table[3]/tbody/tr/td[3]/a')
for link in links:
	urls.append(link.get_attribute('href'))
print(len(urls))

for url in urls[130:145]:
    driver.get(url)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div/ul/li[2]/a').click()
    sleep(1)
    dosen2 = driver.find_elements_by_xpath('//*[@id="dosen"]/table/tbody/tr/td[2]/a')
    for dosen in dosen2:
        urls_dosen.append(dosen.get_attribute('href'))

print(len(urls_dosen))

nama = []
semester = []
kode_matakuliah = []
mata_kuliah = []

for url_dosen in urls_dosen:
    driver.get(url_dosen)
    driver.find_element_by_xpath('//*[@id="tab-data1"]/li[2]/a').click()
    sleep(1)
    nomor = []
    no = driver.find_elements_by_xpath('//*[@id="riwayatmengajar"]/table/tbody/tr/td[1]')
    for nom in no:
        nomor.append(nom.get_attribute('text'))
    b = len(nomor)
    n = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]').text
    a = [n]*b
    for i in range(len(a)): 
        nama.insert(len(nama), a[i]) 
    #nama.append(a)
    print(len(nomor))
    #sleep(1)
    sem = driver.find_elements_by_xpath('//*[@id="riwayatmengajar"]/table/tbody/tr/td[2]')
    for se in sem:
        semester.append(se.text)
    kode = driver.find_elements_by_xpath('//*[@id="riwayatmengajar"]/table/tbody/tr/td[3]')
    for kod in kode:
        kode_matakuliah.append(kod.text)
    mata = driver.find_elements_by_xpath('//*[@id="riwayatmengajar"]/table/tbody/tr/td[4]')
    for matkul in mata:
        mata_kuliah.append(matkul.text)
    #sleep(1)
    print(len(a))
    print(len(nama))
    print(len(semester))
    print(len(kode_matakuliah))
    print(len(mata_kuliah))
    
import pandas as pd
df = pd.DataFrame({'Nama':nama,
                   'Semester':semester,
                   'Kode_Mata_Kuliah':kode_matakuliah,
                   'Mata_Kuliah':mata_kuliah})

print(df)
df.to_json('data_forlap12.json')
driver.close()

#save to sql
#from sqlalchemy import create_engine

#engine = create_engine('sqlite:////home/laila/Desktop/SQL/data_forlap_dosen_mata_kuliah.sql')
#con = engine.connect()
#df.to_sql('data_forlap_dosen_mata_kuliah', con=con, if_exists='replace')