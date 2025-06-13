# NgrokTunnel 🌐

![Streamlit](https://img.shields.io/badge/Streamlit-Deploy%20Live%20Apps-blue?style=flat-square) ![Ngrok](https://img.shields.io/badge/Ngrok-Tunnel%20Service-green?style=flat-square) ![Google Colab](https://img.shields.io/badge/Google%20Colab-Cloud%20Notebook-orange?style=flat-square)

Welcome to the **NgrokTunnel** repository! This project demonstrates how to deploy a live Streamlit web app directly from Google Colab using ngrok for public access. Since Colab doesn’t expose ports externally, ngrok creates a secure tunnel, allowing anyone to interact with your app via a temporary public URL.

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Usage](#usage)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [How It Works](#how-it-works)
7. [Example](#example)
8. [Contributing](#contributing)
9. [License](#license)
10. [Releases](#releases)
11. [Contact](#contact)

## Introduction

In the age of cloud computing, rapid prototyping and sharing ideas has never been easier. With tools like Google Colab, you can write and run Python code in your browser without any setup. However, sharing a live web app built with Streamlit directly from Colab can be challenging. This repository addresses that challenge by utilizing ngrok, a powerful tool that creates secure tunnels to localhost.

## Getting Started

To get started with NgrokTunnel, you need a Google account to access Google Colab. You will also need to install the required packages and set up ngrok to create a tunnel for your Streamlit app.

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AlexQuinhuang/NgrokTunnel.git
   cd NgrokTunnel
   ```

2. **Open Google Colab:**

   Go to [Google Colab](https://colab.research.google.com/) and create a new notebook.

3. **Copy the code:**

   Copy the provided code from this repository into your Colab notebook.

4. **Run the code:**

   Execute the code cells to start your Streamlit app and ngrok tunnel.

5. **Access your app:**

   After running the code, you will receive a public URL. Click on the URL to access your live Streamlit app.

## Requirements

- Python 3.x
- Google Colab
- Streamlit
- ngrok
- pyngrok

## Installation

To install the required packages, run the following commands in your Google Colab notebook:

```python
!pip install streamlit
!pip install pyngrok
```

## How It Works

1. **Streamlit App:** You write your Streamlit app code in a Python script.
2. **Ngrok Tunnel:** Ngrok creates a secure tunnel from your local machine to the public internet. This allows users to access your app through a temporary URL.
3. **Colab Integration:** Google Colab runs your code in the cloud, but it does not expose ports. Ngrok bridges this gap.

## Example

Here’s a simple example of a Streamlit app:

```python
import streamlit as st

st.title("Hello, World!")
st.write("This is a live Streamlit app running from Google Colab!")
```

To run this app, use the following code in your Colab notebook:

```python
from pyngrok import ngrok

# Start ngrok
public_url = ngrok.connect(port='8501')
print(f" * ngrok tunnel \"{public_url}\" -> \"http://localhost:8501\"")

!streamlit run your_app.py &

# Keep the notebook running
import time
while True:
    time.sleep(1)
```

Replace `your_app.py` with the name of your Streamlit app file.

## Contributing

We welcome contributions! If you have suggestions or improvements, please fork the repository and submit a pull request. Make sure to follow the coding standards and include tests for your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Releases

For the latest releases, please visit the [Releases](https://github.com/AlexQuinhuang/NgrokTunnel/releases) section. You can download and execute the necessary files from there.

## Contact

If you have any questions or feedback, feel free to reach out to the project maintainer.

---

This README provides a comprehensive guide to using the NgrokTunnel repository. With clear instructions and examples, you can quickly set up your own Streamlit app using Google Colab and ngrok. Enjoy building and sharing your web applications!