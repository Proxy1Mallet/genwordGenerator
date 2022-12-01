class genwordGenerator:
    def __init__(self):
        self.Session = __import__('requests').Session()
        self.url = 'https://genword.ru/generators/{}/new/'.format
        self.headers = {
            'user-agent': __import__('fake_useragent').UserAgent()['Opera'],
            'x-requested-with': 'XMLHttpRequest'
        }

    def anime(self):
        req = self.Session.post(self.url('anime'), headers = self.headers).json()['result']
        nameEn = req['nameEn']
        nameRu = ['nameRu']
        return  nameRu, nameRu

    def words(self):
        req = self.Session.post(self.url('word'), headers=self.headers).json()['result']
        return req['word']

    def winged(self):
        req = self.Session.post(self.url('winged'), headers=self.headers).json()['result']
        phrase = req['phrase']
        source = req['source']
        return phrase, source

    def alcoholDrinking(self):
        req = self.Session.post(self.url('alcohol-drinking'), headers=self.headers).json()['result']
        nameRu = req['nameRu']
        nameEn = req['nameEn']
        typeAlcohol = req['typeAlcohol']
        return nameRu, nameEn, typeAlcohol

    def alias(self, alias, sex):
        data = {'alias': alias, 'sex': sex}
        req = self.Session.post(self.url('alias'), headers = self.headers, data = data).json()['result']
        return req['alias']

    def slogan(self, slogan):
        data = {slogan: slogan}
        req = self.Session.post(self.url('slogan'), headers=self.headers, data=data).json()['result']
        return req

    def login(self, firstname, surname, patronymic, nickname):
        data = {'firstname': firstname, 'surname': surname, 'patronymic': patronymic, 'nickname': nickname}
        req = self.Session.post(self.url('login'), headers=self.headers, data=data).json()['result']
        return req[0]['login']

print(genwordGenerator().login('Proxy', 'Mallet', 'Kursedovich', 'ProxyMallet'))