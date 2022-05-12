import os
import pickle

import gui.app as app

path = os.getenv('APPDATA') + "\data.pkl"

def searchPassword(input):
  name = input.get()
  elements = getPasswords()
  app.list.delete(0, "end")
  for element in elements:
    if name.lower() in elements[element]["title"].lower():
      app.list.insert("end", elements[element]["title"])

def deletePassword(id):
  passwords = getPasswords()
  del passwords[id]
  savePasswords(passwords)
  return id

def addPassword(password):
  passwords = getPasswords()
  password["id"] = len(passwords) + 1
  passwords[len(passwords) + 1] = password
  savePasswords(passwords)
  return password


def savePasswords(passwords):
  serializedPasswords = pickle.dumps(passwords)
  with open(path, "wb") as dataFile:
    dataFile.write(serializedPasswords)
  return serializedPasswords


def getPasswords():
  if not os.path.exists(path):
    with open(path, "wb") as dataFile:
      dataFile.write(pickle.dumps({}))
    return {}

  if os.path.getsize(path) < 0:
    return {}
  
  try:
    with open(path, "rb") as dataFile:
      data = pickle.loads(dataFile.read())
      return data
  except:
    print(Exception)
    return {}


