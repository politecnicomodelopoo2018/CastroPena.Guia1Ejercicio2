from BD import *
class Liga(object):

    id = None
    nombre = None
    IDPaisPertenecer = None

    def __init__(self):

        self.lista_equipos=[]

    def crearLiga(self,nom,idPais):

        self.nombre=nom
        self.IDPaisPertenecer=idPais




    def setLiga(self):

        cursor=BD().run("Insert into Liga(idLiga, Nombre, Pais_idPais) values (null, '"+self.nombre+"','"+str(self.IDPaisPertenecer)+"');")
        self.id = cursor.lastrowid

    def updateLiga(self):

        BD().run("Update Liga Set Nombre = '"+self.nombre+"', Pais_idPais = '" +str(self.IDPaisPertenecer)+"' where idLiga = '"+str(self.id)+"';")

    def deleteLiga(self):

        contEquipo = BD().run("Select count(*) from Equipo where Liga_idLiga = '" + str(self.id) + "';")

        cont1 = None

        for item in contEquipo:

            cont1 = item["count(*)"]


        if(cont1 == 0):

            BD().run("Delete from Liga where idLiga = '"+str(self.id)+"';")

        else:

            print("No se puede eliminar porque tiene Equipos asociados a la Liga")

    @staticmethod
    def getLiga(unID):
        d = BD().run("Select * from Liga where idLiga = '" + str(unID) + "';")
        lista = d.fetchall()
        UnLiga = Liga()

        UnLiga.id = lista[0]["idLiga"]
        UnLiga.nombre = lista[0]["Nombre"]
        UnLiga.IDPaisPertenecer = lista[0]["Pais_idPais"]

        return UnLiga

    @staticmethod
    def getLigas():

        d=BD().run("select * from Liga;")

        lista_aux=[]

        for item in d:

            lista_aux.append(item)

        return lista_aux