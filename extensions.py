K = input("File name:").lower().strip()

def extension(W):
   ext_w = W.split(".")[-1]
   return ext_w


if K.endswith((".jpg", ".jpeg", ".png", ".gif")):
   x = extension(K)
   print("image/" + x )

elif K.endswith((".pdf", ".zip")):
   x = extension(K)
   print("application/" + x )

elif K.endswith((".txt")):
     print("text/plain")

else:
   print("application/octet-stream")





