
# ConvoBot - Smart Conversational Assistant 🤖💬

**ConvoBot** is a conversational AI built using **Streamlit** and **machine learning models** to provide real-time interactive chat experiences. It allows users to engage in dynamic conversations with AI, offering both streaming and non-streaming responses.

## Features

- **Real-time Chat Streaming**: Provides a live chat experience where responses update as the assistant is generating them.
- **Customizable Models**: Select from various machine learning models for different conversational styles.
- **Interactive UI**: Built with Streamlit, the app provides an intuitive interface for seamless interaction.
- **Message History**: Maintains a chat history to ensure smooth interactions even across multiple sessions.
- **Custom Styling**: Tailored CSS for a visually appealing and user-friendly experience.

## Technologies Used

- **Streamlit**: Framework for creating the interactive user interface.
- **Python**: Backend programming language for logic and API requests.
- **Requests**: Used for making API calls to the backend.
- **HTML/CSS**: Custom styles for the chat interface.
- **AI Models**: Various machine learning models for processing user inputs and generating responses.

## Requirements

- Python 3.10
- Streamlit
- Requests

To install the required libraries, run:

```bash
pip install -r requirements.txt
```

## Setup Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/vishwateja2502/ConvoBot.git
    cd ConvoBot
    ```

2. **Install dependencies**:

    If you haven't installed the required packages yet, do so by running:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:

    To start the app, run:

    ```bash
    streamlit run app.py
    ```

4. **Backend Setup** (if applicable):
    - Ensure that your backend API (e.g., a local server running at `http://localhost:11434`) is set up to handle the requests from the front end.
    - Modify `BACKEND_URL` in the Streamlit code to match the API URL.

## Usage

- Open the app in your browser, and start chatting with the AI!
- You can customize the model and toggle streaming responses from the sidebar.
- The app will keep a chat history, making it easy to review past interactions.

## Demo

Here is a demo GIF showing the UI of ConvoBot during testing:

![ConvoBot UI Demo](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmhsaHZ0b3k3NmI2dmtxeXo0MnI1ZjJtemcya2k0aGEzdDZodmYwNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Q4p6hab6bWsnBLMkDo/giphy.gif)

This demonstrates the real-time interaction and functionality of the chat UI.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
