from db import DBConnection as mydb

class Matakuliah:

    def __init__(self):
        self.__id=None
        self.__kodemk=None
        self.__namamatakuliah=None
        self.__sks=None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def id(self):
        return self.__id

    @property
    def kodemk(self):
        return self.__kodemk

    @kodemk.setter
    def kodemk(self, value):
        self.__kodemk = value

    @property
    def namamatakuliah(self):
        return self.__namamatakuliah

    @namamatakuliah.setter
    def namamatakuliah(self, value):
        self.__namamatakuliah = value

    @property
    def sks(self):
        return self.__sks

    @sks.setter
    def sks(self, value):
        self.__sks = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kodemk, self.__namamatakuliah, self.__sks)
        sql="INSERT INTO matakuliah (kodemk, namamatakuliah, sks) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__kodemk, self.__namamatakuliah, self.__sks, id)
        sql="UPDATE matakuliah SET kodemk = %s, namamatakuliah = %s, sks=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByKODEMK(self, kodemk):
        self.conn = mydb()
        val = (self.__namamatakuliah, self.__sks, kodemk)
        sql="UPDATE matakuliah SET namamatakuliah = %s, sks= %s WHERE kodemk=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM matakuliah WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByKODEMK(self, kodemk):
        self.conn = mydb()
        sql="DELETE FROM matakuliah WHERE kodemk='" + str(kodemk) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM matakuliah WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kodemk = self.result[1]
        self.__namamatakuliah = self.result[2]
        self.__sks = self.result[3]
        self.conn.disconnect
        return self.result

    def getByKODEMK(self, kodemk):
        a=str(kodemk)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM matakuliah WHERE kodemk='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kodemk = self.result[1]
            self.__namamatakuliah = self.result[2]
            self.__sks = self.result[3]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kodemk = ''
            self.__namamatakuliah = ''
            self.__sks = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM matakuliah"
        self.result = self.conn.findAll(sql)
        return self.result
    