
import pyrebase

config={
    "apiKey": "AIzaSyCIFPQHlmOeGSx2bb5ipxmFl7g_TsRuhlw",
    "authDomain": "cctv-46183.firebaseapp.com",
    "projectId": "cctv-46183",
    "storageBucket": "cctv-46183.appspot.com",
    "messagingSenderId": "224356173278",
    "appId": "1:224356173278:web:6755a161c1ed679656494f",
    "measurementId": "G-6RN7WDZT8F",
    "serviceAccount":"./firebase/serviceAccount.json",
    "databaseURL":"https://cctv-46183-default-rtdb.asia-southeast1.firebasedatabase.app"
    }

firebase=pyrebase.initialize_app(config)

# storage=firebase.storage()
# #first write database name and file name in firebase to upload
# # Local path to the image file
# local_image_path = "./firebase/img.webp"

# # Destination path in Firebase Storage
# destination_path = "images/image.jpg"
# # Upload the image
# try:
#     storage.child(destination_path).put(local_image_path)
#     print("Image uploaded successfully!")
# except Exception as e:
#     print(f"Error uploading image: {e}")

# # Download the image
# try:
#     storage.child("images").download(destination_path,"downloaded.jpg")
#     print("Image downloaded successfully!")
# except Exception as e:
#     print(f"Error downloading image: {e}")


db=firebase.database()
# data={
#     "email":"h67dabhi@gmail.com",
#     "password":"harsh",
#     "SystemOn":"False",
#     "Alert":"False"
# }
# db.child("h67dabhi").set(data)


# user = db.child("Darshan").get()
# for i in user.each():
#    if i.key()=="SystemOn":
#         if i.val()=="True":
#             print(i.val())



# user = db.child("Darshan").update({"SystemOn": "True"})


user = db.child("h67dabhi").get()

print(user.val())
