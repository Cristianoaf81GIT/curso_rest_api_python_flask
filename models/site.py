from sql_alchemy import banco


class SiteModel(banco.Model):
    __tablename__ = 'sites'

    site_id = banco.Column(banco.Integer, primary_key=True)
    url = banco.Column(banco.String())
    # cria um relacionamento entre duas tabelas/entidades 
    # obtem lista de objetos hoteis relacionados ao modelo siteModel (automatico)
    hoteis = banco.relationship('HotelModel')  
  
    def __init__(self, url):
        self.url = url        

    # transform into dicitionary/json
    def json(self):
        return {
            'site_id': self.site_id,
            'url': self.url,
            'hoteis': [hotel.json() for hotel in self.hoteis]
        }

    @classmethod
    def find_site(cls, url):
        site = cls.query.filter_by(url=url).first()
        if site:
            return site
        return None

    def save_site(self):
        banco.session.add(self)
        banco.session.commit()

 
    def delete_site(self):
        banco.session.delete(self)
        banco.session.commit()
