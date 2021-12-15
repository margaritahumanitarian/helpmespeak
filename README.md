# Helpmespeak

---

**Help me speak** uses Python functions for summarizing and improving voice dictation input.

## Get started with OpenAI gpt-3

---

OpenAI is a amazing tool with lot of features and ability available to a developer. Follow the official [documentation](https://beta.openai.com/docs/introduction) and play with it.

Here is an example of OpenAI gpt3

#### prompt

> Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.
> Jupiter is primarily composed of hydrogen with a quarter of its mass being helium, though helium comprises only about a tenth of the number of molecules. It may also have a rocky core of heavier elements,[21] but like the other giant planets, Jupiter lacks a well-defined solid surface. Because of its rapid rotation, the planet's shape is that of an oblate spheroid (it has a slight but noticeable bulge around the equator).
> tl;dr:

Response from the API : -

> Jupiter is the largest planet in the solar system. It is a gas giant, and is the fifth planet from the sun.

See few more **[example](https://beta.openai.com/docs/examples/summarization)** for **OpenAI gpt3**.

## Installation

---

### 1. Clone the repository from GitHub

Choose your prefered way to clone, either:
`git clone https://github.com/margaritahumanitarian/helpmespeak.git`
or
`git clone git@github.com:margaritahumanitarian/helpmespeak.git`

Go to the cloned directory:

` cd helpmespeak/`

### 2. Install OpenAI Python library

To install the official Python bindings, run the following command:
`pip install openai`

### 3. Setup .evn file

create a `.env` file in the root directory of the project and paste the content of [`.env.example`]() in the newly created `.env` file.
Replace `YOUR_API_KEY` with your `openAI API`

**Note:** You can get your Api Key from *https://beta.openai.com/account/api-keys*

## Usage

---
