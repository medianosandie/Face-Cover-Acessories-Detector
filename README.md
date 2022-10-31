# Face-Cover-Acessories-Detector
## Petunjuk Instalasi
Model yang digunakan pada penelitian ini adalah model YOLOV5s yang menggunakan algoritma YOLOV5 untuk melakukan object detection, model ini dibuat oleh ultralytics. Model ini sebelumnya sudah dilatih di dataset COCO yang terdiri dari 80 kelas. Pada penelitian ini penulis menggunakan custom dataset yang penulis kumpulkan sendiri dan unduh dari website Kaggle. Proses model training sendiri dilakukan di Google Colaboratory, karena lebih mudah untuk digunakan dan tidak perlu melakukan setup environment yang rumit, dan juga dapat mengakses resource google melalui cloud seperti GPU yang dapat mempercepat proses training. Untuk menggunakan model ini pertama load model menggunakan bantuan library Pytorch, kemudian simpan hasil kemabalianya kedalam sebuah variabel untuk memudahkan proses pemanggilan. Setelah menyiapkan model yang akan di train ulang menggunakan custom dataset yang telah dibuat sebelumnya, selanjutnya load dataset menggunakan bantuan module Roboflow untuk kemudian diunduh dan disimpan di penyimpanan. Spesifikasikan mengenai detail dari dataset didalam file dataset.yml, lalu simpan file ini kedalam direktori yolov5. Setelah itu proses training dapat dilakukan dengan menjalankan file train.py didalam direktori yolov5. Pada saat menjalankan file train.py spesifikasian juga ukuran dari gambar, jumlah batch, path menuju  file dataset.yml, path menuju weight yang akan digunakan.
Proses training dilakukan di Google Colaboratory untuk itu pertama buat notebook baru terlebih dahulu, lalu buat code cell baru dengan kode seperti pada gambar dibawah untuk melakukan clone terhadap repository YOLOV5 dan mengunduh dan menginstall library Pytorch
Untuk mengunduh seluruh dependencies pertama jalankan seluruh code cell yang ada didalam file download_dependencies.ipynb
Setelah itu jalankan code cell yang ada di file notebook train_model.ipynb sampai sebelum heading “Training model on custom dataset”
Sebelum melatih model buka root directory dari file notebook kemudian masuk ke direktori “yolov5” dan hapus file dataset.yml. Buat ulang file dataset.yml lalu unggah Kembali ke direktori ditempat diman file dataset.yml sebelumnya berada yaitu di direktori “yolov5”. 
![]( https://github.com/medianosandie/Face-Cover-Acessories-Detector/blob/main/img/1.jpg)
<p align="center">
  **Gambar** file dan subdirektori yang ada pada direktori yolov5
<p>
Latih model pada dataset menggunakan command berikut. Model akan dilatih menggunakan weight yolo5m sebanyak 300 epoch, dan dataset akan dibagi menjadi 16 batch.
![]( https://github.com/medianosandie/Face-Cover-Acessories-Detector/blob/main/img/2.jpg)
<p align="center">
  **Gambar** code cell beserta kode untuk melatih model pada custom dataset
<p>

Setelah berhasil menalankan seluruh code cell tersisa, download weight file last.pt dan best.pt untuk kemudian di-load pada model yang akan digunakan di aplikasi
![]( https://github.com/medianosandie/Face-Cover-Acessories-Detector/blob/main/img/3.jpg)
<p align="center">
  **Gambar** lokasi file best.pt pada root directory
<p>
## Prediksi
Untuk melakukan prediksi pertama load weight dari model yang sudah dilatih dari custom dataset sebelumnya menggunakan bantuan Pytorch dengan memasukkan path ke file weight sebagai parameter ketiga dan ‘custom’ sebagai parameter kedua. Prediksi dapat dilakukan dengan memasukkan path gambar yang ingin di prediksi sebagai parameter pada objek model

## Membuat Tampilan GUI dan Menambahkan Fungsionalitas ke Aplikasi Desktop
Disini penulis membuat aplikasi desktop menggunakan bantuan library pyhon Tkinter. Langkah pengerjaanya, pertama buat sebuah file python baru dengan  nama detector.py. Setelah file berhasil dibuat, import library yang dibutuhkan seperti tkinter, os, PIL, torch, glob, numpy, dan numpy. Setelah itu buat sebuah class bernama Window yang didalamnya terdapat function-function berikut: __init__, backToMenu, ResizeWithAspectRatio, predict_vid_Page, predict_img_Page, browseFiles, Restore, detect_img 

## Petunjuk Penggunaan
Untuk menggunakan aplikasi, pertama buka command prompt di direktori project
![]( https://github.com/medianosandie/Face-Cover-Acessories-Detector/blob/main/img/4.jpg)

Lalu aktifkan virtual environment
![]( https://github.com/medianosandie/Face-Cover-Acessories-Detector/blob/main/img/5.jpg)

Kemudian jalankan aplikasi dengan cara mengetikkan command ‘python detector.py’
![]( https://github.com/medianosandie/Face-Cover-Acessories-Detector/blob/main/img/6.jpg)

Maka aplikasi akan terbuka dengan tampilan halaman menu utama seperti pada gambar berikut:
![]( https://github.com/medianosandie/Face-Cover-Acessories-Detector/blob/main/img/7.jpg)
<p align="center">
  **Gambar** tampilan halaman utama aplikasi
</p>

Pilih salah satu menu untuk melakukan prediksi. Klik tombol predikasi gambar untuk melakukan prediksi gambar dan tombol video untuk melakukan prediksi video realtime melalui webcam.
![]( https://github.com/medianosandie/Face-Cover-Acessories-Detector/blob/main/img/8.jpg)
<p align="center">
  **Gambar** tampilan halaman prediksi gambar
</p>

Di halaman prediksi gambar, terdapat tiga tombol, untuk melakukan prediksi pertama pilih file gambar yang ingin diprediksi dengan mengklik tombol browser image files, maka popup window select file akan terbuka, pilih file gambar yang ingin dipilih. Setelah gambar dipilih, maka gambar tersebut akan muncul di bagian tengah window, untuk melakukan prediksi terhadap gambar yang dipilih klik predict image, maka hasil gambar yang telah diprediksi akan muncul dibagian tengah window, hasil deteksi objek akan ditandai dengan bounding box.untuk Kembali ke menu utama ke tombol back.
![]( https://github.com/medianosandie/Face-Cover-Acessories-Detector/blob/main/img/9.jpg)
<p align="center">
  **Gambar** tampilan webcam
</p>
![]( https://github.com/medianosandie/Face-Cover-Acessories-Detector/blob/main/img/10.jpg)
<p align="center">
  **Gambar** tampilan halaman prediksi video
</p>
Pada saat tombol prediksi video diklik maka window predict video dan webcam akan otomatis terbuka. Webcam akan otomatis mendeteksi objek yang muncul di webcam dengan menandai objek dengan bounding box beserta level confidencenya (apabila nilai confidence mendekati 1 artinya model makin yang adalah objek yang ditandai dengan bounding box). Untuk menutup webcam klik q , dan untuk Kembali ke halaman utama klik tombol back untuk Kembali ke main menu.

## Tampilan Beberapa Hasil Prediksi
![]( https://github.com/medianosandie/Face-Cover-Acessories-Detector/blob/main/img/11.jpg)

![]( https://github.com/medianosandie/Face-Cover-Acessories-Detector/blob/main/img/12.jpg)
