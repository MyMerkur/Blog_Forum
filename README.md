# Blog_Forum

https://blogforum--mymerkur.repl.co

Bu proje, Django, JavaScript, JSON, SCSS ve Bootstrap kullanılarak geliştirilmiş bir blog-forum uygulamasını içerir. Proje, kullanıcıların yazılar paylaşabileceği, yorum yapabileceği ve toplulukla etkileşimde bulunabileceği bir platform sunar.

## Tr

Proje, kullanıcıların yazılarını ve düşüncelerini paylaşabileceği bir blog özelliği sunar. Ayrıca, kullanıcıların farklı konularda tartışabileceği bir forum özelliği de içerir. Ana sayfa, dinamik olarak JSON formatındaki verileri kullanarak en son yazıları ve forum gönderilerini görüntüler.

### Kullanılan Teknolojiler

- Django: Web uygulaması geliştirmek için kullanıldı.
- JavaScript: Kullanıcı etkileşimi için kullanıldı.
- JSON: Verilerin dinamik olarak yüklenmesi için kullanıldı.
- SCSS ve Bootstrap: Arayüz tasarımı için kullanıldı.

### Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1. Proje deposunu klonlayın.
2. Virtualenv kullanarak bir sanal ortam oluşturun.
3. Gerekli bağımlılıkları yüklemek için `pip install -r requirements.txt` komutunu kullanın.
4. Veritabanını oluşturmak için `python manage.py migrate` komutunu çalıştırın.
5. Projeyi başlatmak için `python manage.py runserver` komutunu kullanın.

### Kullanım

Projeyi başlattıktan sonra, tarayıcınızdan `http://localhost:8000` adresine giderek blog ve forum özelliklerini kullanabilirsiniz.

## En

This project includes a blog-forum application developed using Django, JavaScript, JSON, SCSS, and Bootstrap. The project provides a platform where users can share posts, comment, and interact with the community.

### Features

The project includes the following features:

- Blog: Allows users to share their thoughts and posts.
- Forum: Allows users to discuss various topics.
- Dynamic Content: The homepage displays the latest posts and forum discussions dynamically using JSON.

### Technologies Used

- Django: Used for web application development.
- JavaScript: Used for user interaction.
- JSON: Used for dynamic data loading.
- SCSS and Bootstrap: Used for interface design.

### Installation

To run the project on your local machine, follow these steps:

1. Clone the project repository.
2. Create a virtual environment using Virtualenv.
3. Use `pip install -r requirements.txt` to install the necessary dependencies.
4. Run `python manage.py migrate` to create the database.
5. Start the project using `python manage.py runserver`.

### Usage

After starting the project, you can use the blog and forum features by visiting `http://localhost:8000` in your browser.
![Ekran Resmi 2023-09-27 11 39 43](https://github.com/MyMerkur/Blog_Forum/assets/116354050/ec28eab3-90de-4ecd-a379-eafc072528a1)
