from django.db import models
import pydoop.hdfs as hdfs
import pymongo

class InstanceItem(models.Model):

	MAXGET = 10
	connection = None
	db = None
	collection = None
	urlList = None

	def __init__(self):
		self.connectDB()

	def ls_cmd(self, dirname):
		ls_list = hdfs.ls(str(dirname))
		return ls_list

	def connectDB(self):
		self.connection = pymongo.MongoClient("localhost", 27017)
		self.db = self.connection.crawler_db
		self.collection  = self.db.urlCollection

	def removeFileFromPath(self,path) :

		ls_list = hdfs.lsl(path)
		ls_count = len(ls_list)

		if ls_count != 0 :
			hdfs.rmr(path,"hdfs")

	def getInstanceList_model(self,dirname):

		ls_list = hdfs.lsl(dirname)
		ls_count = len(ls_list)
		instanceList = []

		for item in ls_list:

			splitName = item["name"].split("/")
			if len(splitName) > 0 :
				instanceFolderName = splitName[len(splitName)-1]
				item["name"] = instanceFolderName
				instanceList.append(item)

		return instanceList

	def getInstanceItems_model(self, dirname, offset=0):

		i = 0
		ls_list = hdfs.lsl(dirname)
		ls_count = len(ls_list)
		instanceList = []

		for item in ls_list:
			splitName = item["name"].split("/")
			if len(splitName) > 0 :
				fullName = splitName[len(splitName)-1]
				instanceID = fullName.split(".")[0]

				docs = self.collection.find({"file_id":instanceID})
				instance = None
				for obj in docs:
					#objectItem =  JSONEncoder().encode(docs)
					instance = {"url":obj["url"], "instance_id":obj["instance_id"], "file_id":obj["file_id"], "crawl_name":obj["instance_name"], "hdfs_path":dirname+"/"+obj["file_id"]+".jpg"}

				if instance != None:
					instanceList.append(instance)


		return instanceList

# Create your models here.
