# Peter Moss MedTech Research Project
## GPT-3 Leukemia Information Assistant
### Getting Started

![GPT-3 Leukemia Information AssistantGPT-3 Leukemia Information Assistant](../assets/images/project-banner.jpg)

&nbsp;

# Table Of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [OpenAI API Beta](#openai-api-beta)
- [Configuration](#configuration)
- [Testing](#testing)
  - [Answers](#answers)
  - [Completions](#completions)
  - [Server](#server)
- [Article](#article)
- [Contributing](#contributing)
  - [Contributors](#contributors)
- [Versioning](#versioning)
- [License](#license)
- [Bugs/Issues](#bugs-issues)

&nbsp;

# Introduction
This guide will guide you through the installation process for the GPT-3 Leukemia Information Assistant.

&nbsp;

# Installation
First you need to install the required software for training the model. Below are the available installation guides:

- [Ubuntu installation guide](installation/ubuntu.md) (Training).

&nbsp;

# OpenAI API Beta
To use this project you will need an account for the [OpenAI API Beta](https://beta.openai.com/).

&nbsp;

# Configuration
[configuration/config.json](../configuration/config.json "configuration/config.json")  holds the configuration for our application.

- Change **agent->server** to the local IP of your training device.
- Change **agent->port** to a different number.
- Change **openai->key** to your OpenAI Beta key.

<details><summary><b>View file contents</b></summary>
<p>

```
{
    "agent": {
        "cores": 8,
        "params": [
            "answer",
            "completion",
            "server"
        ]
    },
    "openai": {
        "engine": "davinci",
        "temperature": 0.9,
        "max_tokens": 150,
        "top_p": 1,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.6,
        "key": "",
        "url": "https://api.openai.com/v1"
    }
}
```

</p>
</details>

&nbsp;

# Testing

The GPT-3 Leukemia Information Assistant has three interaction modes: **answers**, **completions** and **server**.

## Answers

Answers is an API endpoint that generates answers to questions, you can find out more about the Answers API on [this link](https://beta.openai.com/docs/api-reference/answers).

Below are some **answers** examples using the GPT-3 Leukemia Information Assistant.

```
python3 agent.py answer "How many people died from leukemia in 2020?"
2021-05-29 04:41:06,004 - Agent - INFO - In 2020, approximately 312,000 individuals died with this disease.
```

```
python3 agent.py answer "What is Acute Myeloid Leukemia?"
2021-05-29 04:42:48,819 - Agent - INFO - Acute myeloid leukemia (AML) is a rapid-growing form of cancer that affects white blood cells called myeloid cells. AML occurs in adults as well as children.
```

```
python3 agent.py answer "What are the types of leukemia?"
2021-05-29 04:52:47,877 - Agent - INFO - Leukemia can be categorized into 3 major types based on their development stage: Acute lymphoblastic leukemia (ALL), chronic lymphocytic leukemia (CLL) and acute myeloid leukemia (AML).
```

## Completions

Completions is an API endpoint that is able to complete some information given a prompt, you can find out more about the Answers API on [this link](https://beta.openai.com/docs/api-reference/completions).

Below are some **completions** examples using the GPT-3 Leukemia Information Assistant.

```
python3 agent.py completion "Leukemia is"
2021-05-29 05:01:10,469 - Agent - INFO -  a cancer that begins in the bone marrow and spreads to other parts of the body, such as the lymph nodes, liver and spleen. Many forms of leukemia are treated with chemotherapy, a type of medicine that treats cancer by killing cancer cells or stopping them from multiplying. People with leukemia may also receive radiation therapy, which uses high-energy x-rays and other types of radiation to kill cancer cells and shrink tumors.
```

```
python3 agent.py completion "Acute Myeloid Leukemia is"
2021-05-29 05:01:34,636 - Agent - INFO -  a cancer of the white blood cells. Approximately each year about people in the US are diagnosed with AML. Of those people, , will try conventional treatments first. This is because conventional cancer treatments are based upon an antiquated model of cancer that few understand, thus making it more difficult for them to trust their medical advisors. In the case of cancer, this leads to much suffering (morale) and higher costs to the patient, who may also have to deal with a reduced quality of life if conventional treatment doesn't work. Acute Myeloid Leukemia originates in the bone marrow, which are the spongy, marrow-filled cavities found inside your bones.
```

```
python3 agent.py completion "Acute Lymphoblastic Leukemia is"
2021-05-29 05:01:56,343 - Agent - INFO -  the most common type, and is the kind that primarily impacts children. This disease is considered a slow, albeit steadily progressing one, because it can last for many years before cancerous cells develop. The last tissue affected when this happens is bone marrow.
```

## Server

The server mode allows you to expose the GPT-3 Leukemia Information Assistant via a REST API. This mode only returns answers.

In the current terminal, use the following command:

```
python3 agenty.py server
```

This will start the server on your machine that exposes the model via a REST API. Now open a new terminal, navigate to the project root and use the following command:

```
python3 client.py "What is Acute Myeloid Leukemia?"
2021-05-29 05:04:37,319 - Client - INFO - Response: "Acute myeloid leukemia (AML or acute myeloid leukemia, AML for short) is the most common type of acute leukemia, a cancer of the blood. It originates in the bone marrow, the soft inner part of most bones, and effects the formation of blood cells in the body. (Reference is from: http://www.seer.cancer.gov/faststats/selections.php?index=148)"
```

&nbsp;

# Article
In the following weeks I will be working with our medical advisor [Rita Silva](https://www.leukaemiamedtechresearch.org.uk/about/volunteers/rita-silva-md-phd "Rita Silva") to write an article based on this project. We will discuss the accuracy of GPT-3 and whether or not it may have potential in it's current state to be used for medical advice. Please note that at this moment it is currently against OpenAI's [use case guidelines](https://beta.openai.com/docs/use-case-guidelines/faq) to create a production application that is intended to provide medical advice.

&nbsp;

# Contributing
Peter Moss Leukaemia MedTech Research CIC encourages and welcomes code contributions, bug fixes and enhancements from the Github community.

Please read the [AI AGENT CONTRIBUTING](https://github.com/leukaemiamedtech/contributing-guides/blob/main/CONTRIBUTING-GUIDE-AI-AGENTS.md "AI AGENT CONTRIBUTING") guide for a full guide to contributing to our AI Agent projects. You will also find our code of conduct in the [CODE OF CONDUCT](https://github.com/leukaemiamedtech/contributing-guides/blob/main/CODE-OF-CONDUCT.md) document.

## Contributors
- [Adam Milton-Barker](https://www.leukaemiamedtechresearch.org.uk/about/volunteers/adam-milton-barker "Adam Milton-Barker") - [Peter Moss Leukaemia MedTech Research CIC](https://www.leukaemiamedtechresearch.org.uk "Peter Moss Leukaemia MedTech Research CIC") Founder & Managing Director.

- [Dr Rita Rb-Silva](https://www.leukaemiamedtechresearch.org.uk/about/volunteers/rita-silva-md-phd "Dr Rita Rb-Silva") - [Peter Moss Leukaemia MedTech Research CIC](https://www.leukaemiamedtechresearch.org.uk "Peter Moss Leukaemia MedTech Research CIC") Medical Advisor (Hematology), Porto, Portugal

&nbsp;

# Versioning
We use [SemVer](https://semver.org/) for versioning.

&nbsp;

# License
This project is licensed under the **MIT License** - see the [LICENSE](https://github.com/leukaemiamedtech/hias-all-jetson-nano-classifier/blob/main/LICENSE "LICENSE") file for details.

&nbsp;

# Bugs/Issues
We use the [repo issues](https://github.com/leukaemiamedtech/hias-all-jetson-nano-classifier/issues/new/choose "repo issues") to track bugs and general requests related to using this project. See [AI AGENT CONTRIBUTING](https://github.com/leukaemiamedtech/contributing-guides/blob/main/CONTRIBUTING-GUIDE-AI-AGENTS.md "AI AGENT CONTRIBUTING") guide for more info on how to submit bugs, feature requests and proposals.