# 🐶 Dognet 🐕

Welcome to Dognet! This project is a culmination of my passion for machine learning and web development, showcasing my skills in fine-tuning deep learning models, web application development, and cloud deployment.

## 🚀 Features

- **Deep Learning Model**: Utilized a fine-tuned ResNet-18 model on the Stanford Dogs dataset, consisting of over 20,000 images across 120 breeds. Achieved an impressive accuracy of 82%.
- **Web Application**: Built a user-friendly web app using Flask, allowing users to upload images and receive predictions on dog breeds.
- **Dockerization**: Dockerized the application for easy deployment and platform independence, pushing the Docker image to Docker Hub.
- **Cloud Deployment**: Deployed the web app to Azure, leveraging the Docker image for seamless deployment and scalability.

## 🛠️ Technology Stack

- **Deep Learning**: PyTorch for model fine-tuning and prediction.
- **Web Development**: Flask for creating the web application.
- **Containerization**: Docker for packaging the application.
- **Cloud Deployment**: Azure for hosting the web app.

## 📦 Docker Setup

To run the application locally using Docker, follow these steps:

1. Clone the repository: `git clone https://github.com/skadoosh4/dognet.git`
2. Navigate to the project directory: `cd dognet`
3. Build the Docker image: `docker build -t dognet .`
4. Run the Docker container: `docker run -p 5000:8080 dognet`

## 🐳 Docker Setup

To pull the Docker image from Docker Hub, simply run the following command:

```bash
docker pull skadoosh4/dognet:1.0
```

## 🌐 Deployment on Azure

The web app is deployed on Azure and can be accessed at [your-web-app-url].

## 📸 Screenshots

![Home Page](https://github.com/skadoosh4/dognet/blob/main/images/home.png)
![Prediction Result](https://github.com/skadoosh4/dognet/blob/main/images/prediction.png)

## 📝 License

This project is licensed under the MIT License.

## 👥 Acknowledgments

- Stanford Dogs Dataset for the dataset.
- PyTorch for the deep learning framework.
- Flask for the web framework.
- Docker for containerization.
- Azure for cloud deployment.
