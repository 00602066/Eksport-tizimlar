# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15N3GP-LEzpEZUdkkNy91ERNyQuSAIjWl
"""

def tashxis(belgi):
  if belgi== "istima":
    return "Parasetamol iching"
  elif belgi == "katarakta":
    return "Deksamotazon"
  elif belgi == "gripp":
      return "Taylolhot"
  else:
        return  "SHifokorga murojaat qiling"
belgi= input("kasallik belgisini kiriting: ")
natija=tashxis(belgi)
print(natija)

from google.colab.patches import cv2_imshow
import cv2
def narxi(rusmi):
  if rusmi == "ducatti":
    rasm1=cv2.imread("rasm.jpg")
    cv2_imshow(rasm1)
    return "$25,000 - $30,000 USD"
  elif rusmi == "BMW":
    rasm1=cv2.imread("photo_2020-07-02_11-44-34.jpg")
    cv2_imshow(rasm1)
    return " $24,295 USD"
  elif rusmi == "Kawasaki":
    rasm1=cv2.imread("photo_2021-01-14_20-53-53.jpg")
    cv2_imshow(rasm1)
    return " $30,000+ USD"

rusmi= input("Motoning rusmini kiriting: ")
natija=narxi(rusmi)
print(natija)