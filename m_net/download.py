import pycurlimport requestsimport jsonimport timeimport osdef performMyMulti(tools_, time_frame = ‘1m’):”’Функция многопоточного скачивания. Принимает на вход списоккодов инструментов для скачивания. Количество инструментов в этомсписке не должно превышать 100шт.”’m = pycurl.CurlMulti()m.handles = []files = [] # список файлов для сохранения результатовstart_ = time.time() # замер времени для расчета скорости, начальная точка# создание и настройка curl-объектовfor tool_ in tools_:c = pycurl.Curl()# имя файла для сохранения результатов; файлы сохраняются в каталог datafileName = “data%s%s_%s.txt” % (os.sep, tool_, time_frame)fileName = fileName.replace(‘*’, ‘_’)f = open(fileName, “wb”)files.append(f) # файл добавляется в список, чтобы потом закрыть егоc.setopt(c.WRITEDATA, f) # кроме файла здесь можно указывать функцию, но файл нам наиболее удобенurl = “https://api.iextrading.com/1.0/stock/%s/chart/%s” % (tool_, time_frame)c.setopt(pycurl.URL, url)m.add_handle(c)m.handles.append(c)num_handles = len(m.handles)
while num_handles:
while 1:# выполнить запросы
ret, num_handles = m.perform()
if ret != pycurl.E_CALL_MULTI_PERFORM:
	breakm.select(1.0)# очистка
for c in m.handles:
	c.close()
	m.remove_handle(c)
for f in files:
f.close()
m.close()
del m.handlesend_ = time.time() # замер времени для расчета скорости, конечная точка
return len(tools_) / (end_–start_) # скорость в секунду# скачиваем список инструментов
r = requests.get(‘https://api.iextrading.com/1.0/ref-data/symbols’)
data = json.loads(r.text)tools = [] 
#список кодов инструментов
# выбираем коды инструментов в отдельный массив
for tool in data:
	try:
		if tool[‘isEnabled’] is True:tools.append(tool[‘symbol’])
except:continueblock = 80 #количество параллельных запросов (не более 100шт)tools_count = len(tools)
print(u“Всего инструментов для скачивания: %d” % tools_count)
loops = tools_count / block # количество полных циклов (циклов по block запросов)
tail = tools_count % block # количество оставшихся запросов
tools_ok = # общее количество выполненных запросов
start = time.time() # замер общего времени, начальная точка
for i in range(loops): # в цикле по всем полным циклам
srez = tools[i*block:i*block+block:1] # формируем выборку из следующих block инструментов
speed = performMyMulti(srez) # выполняем параллельное скачивание
tools_ok += blockprint(u“готово %d из %d, скорость %f в сек” % (tools_ok, tools_count, speed))if tail > : # “докачиваем” оставшиеся инструментыi += 1srez = tools[block*i:block*i+tail]
speed = performMyMulti(srez)tools_ok += tailprint(u“готово %d из %d, скорость %f в сек” % (tools_ok, tools_count, speed))
end = time.time() # замер общего времени, конечная точкаprint(u“Всё скачали! Ушло %f сек” % (end–start))