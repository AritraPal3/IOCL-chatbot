# FAQ Provident Fund Chatbot using RASA

Welcome to the FAQ Provident Fund Chatbot project built using the RASA framework! This chatbot is designed to assist users in answering frequently asked questions related to Provident Fund (PF). By utilizing the RASA pipeline and its components, this project aims to provide accurate and efficient responses to user queries.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Training Data](#training-data)
- [Training Pipeline](#training-pipeline)
- [Custom Actions](#custom-actions)
- [Interactive Mode](#interactive-mode)

## Project Overview

This chatbot leverages the power of RASA's natural language understanding and dialogue management to interact with users regarding Provident Fund related inquiries. Users can ask questions about various aspects of PF, such as eligibility criteria, withdrawal process, contribution rates, and more. The chatbot will process the user's input and respond with relevant and accurate information.

## Installation

1. Clone this repository to your local machine using:

   ```bash
   git clone <paste the url here>
   ```

2. Navigate to the project directory:

   ```bash
   cd faq-pf-chatbot
   ```

3. Install the required dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the FAQ Provident Fund Chatbot, follow these steps:

1. Train the chatbot by running:

   ```bash
   rasa train
   ```

2. Start the chatbot server:

   ```bash
   rasa run actions
   ```

3. Start the RASA shell to interact with the chatbot:

   ```bash
   rasa shell
   ```

## Training Data

The training data for the chatbot is located in the `data/` directory. It includes example user messages and their corresponding intents and entities. You can modify and expand this data to improve the chatbot's understanding and responses.

## Training Pipeline

The RASA pipeline configuration can be found in the `config.yml` file. This pipeline includes components for natural language understanding (NLU) and dialogue management.

## Custom Actions

Custom actions, located in the `actions/` directory, allow the chatbot to perform dynamic actions such as fetching external data or invoking APIs. You can extend these actions to enhance the chatbot's capabilities.

## Interactive Mode

You can use RASA's interactive mode to test and refine the chatbot's responses. Run the following command:

```bash
rasa interactive
```


Feel free to explore, modify, and enhance this chatbot project. If you have any questions or need further assistance, please don't hesitate to reach out to the project maintainers. Happy coding!

-- many things are yet to implemented
