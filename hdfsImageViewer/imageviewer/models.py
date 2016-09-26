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
		self.collection  = self.db.urls

	def getInstanceItems(self, dirname, offset=0):

		i = 0
		ls_list = hdfs.ls(dirname)
		ls_count = len(ls_list)
		instanceList = []

		for item in ls_list:
			splitName = item.split("_")
			if len(splitName) > 0 :
				fullName = splitName[1]
				instanceID = fullName.split(".")[0]

				docs = self.collection.find({"instance_id":instanceID})
				instance = None
				for obj in docs:
					#objectItem =  JSONEncoder().encode(docs)
					instance = {"url":obj["url"], "instance_id":obj["instance_id"], "category_id":obj["instance_category"], "category_name":obj["instance_name"]}

				if instance != None:
					instanceList.append(instance)


		return instanceList

# Create your models here.
