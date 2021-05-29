# Asociación de Investigacion en Inteligencia Artificial Para la Leucemia Peter Moss
## GPT-3 Leukemia Information Assistant
### Ubuntu Installation

![GPT-3 Leukemia Information Assistant](../../assets/images/gpt-3-leukemia-assistant.jpg)

&nbsp;

# Table Of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
	- [Anaconda](#anaconda)
- [Installation](#installation)
	- [Intel® Optimization for TensorFlow](#intel-optimization-for-tensorflow)
	- [Clone The Repository](#clone-the-repository)
		- [Developer Forks](#developer-forks)
	- [Setup File](#setup-file)
- [HIAS](#hias)
	- [AI Model](#ai-model)
	- [AI Agent](#ai-agent)
- [Continue](#continue)
- [Contributing](#contributing)
  - [Contributors](#contributors)
- [Versioning](#versioning)
- [License](#license)
- [Bugs/Issues](#bugs-issues)

# Introduction
This guide will guide you through the installation process for the GPT-3 Leukemia Information Assistant.

# Prerequisites
You will need to ensure you have the following prerequisites installed and setup.

## Anaconda
If you haven't already installed Anaconda you will need to install it now. Follow the [Anaconda installation guide](https://docs.anaconda.com/anaconda/install/ "Anaconda installation guide") to do so.

## HIAS Server
For this project you will need a functioning [HIAS Server](https://github.com/AIIAL/HIAS). To install the HIAS Server, follow the [HIAS Server Installation Guide](https://github.com/AIIAL/HIAS/blob/master/Documentation/Installation/Installation.md)

# Installation
You are now ready to install the GPT-3 Leukemia Information Assistant software.

## Intel® Optimization for TensorFlow
Now you will install the Intel® Optimization for TensorFlow using Anaconda.

```
conda create -n all-tfmkl python=3
conda activate all-tfmkl
conda install tensorflow -c anaconda
conda deactivate
```

## Clone the repository

Clone the [GPT-3 Leukemia Information Assistant](https://github.com/AIIAL/GPT-3-Leukemia-Information-Assistant " GPT-3 Leukemia Information Assistant") repository from the [Peter Moss Acute Myeloid & Lymphoblastic Leukemia AI Research Project](https://github.com/AIIAL "Asociación de Investigacion en Inteligencia Artificial Para la Leucemia Peter Moss") Github Organization.

To clone the repository and install the OneAPI Acute Lymphoblastic Leukemia Classifier Classifier, make sure you have Git installed. Now navigate to the a directory on your device using commandline, and then use the following command.

```
 git clone https://github.com/AIIAL/GPT-3-Leukemia-Information-Assistant.git
```

Once you have used the command above you will see a directory called **GPT-3-Leukemia-Information-Assistant** in your home directory.

```
 ls
```

Using the ls command in your home directory should show you the following.

```
 GPT-3-Leukemia-Information-Assistant
```

Navigate to the **GPT-3-Leukemia-Information-Assistant** directory, this is your project root directory for this tutorial.

### Developer Forks

Developers from the Github community that would like to contribute to the development of this project should first create a fork, and clone that repository. For detailed information please view the [CONTRIBUTING](../../CONTRIBUTING.md "CONTRIBUTING") guide. You should pull the latest code from the development branch.

```
 git clone -b "2.0.0" https://github.com/AIIAL/GPT-3-Leukemia-Information-Assistant.git
```

The **-b "2.0.0"** parameter ensures you get the code from the latest master branch. Before using the below command please check our latest master branch in the button at the top of the project README.

## Setup File

All other software requirements are included in **scripts/install.sh**. You can run this file on your machine from the project root in terminal. Use the commands that follow:

```
 conda activate all-tfmkl
 sh scripts/install.sh
 conda deactivate
```

&nbsp;

# HIAS

This device is a HIAS AI Agent and uses the HIAS MQTT Broker to communicate with the HIAS network. To setup an AI Agent on the HIAS network, head to the HIAS UI.

The HIAS network is powered by a context broker that stores contextual data and exposes the data securely to authenticated HIAS applications and devices.

Each HIAS AI Agent & AI Model has a JSON representation stored in the HIAS Context Broker that holds their contextual information.

## AI Model

A HIAS AI Model is a JSON representation of an Artificial Intelligence model used by the HIAS network.

First you need to set a HIAS AI Model up in the HIAS UI. Navigate to **AI->Models->Create** to create a HIAS AI Model. A future release of HIAS will provide the functionality to import the HIAS JSON representation of the AI Model, but for now you have to manually create the AI Model in the UI.

![HIAS AI Model](../../assets/images/hias-ai-model.jpg)

Once you have completed the form and submitted it, you can find the newly created AI Model by navigating to **AI->Models->List** and clicking on the relevant Model.

On the HIAS AI Model page you will be able to update the contextual data for the model, and also find the JSON representation.

![HIAS AI Model](../../assets/images/hias-ai-model-edit.jpg)

## AI Agent

A HIAS AI Agent is a bridge between HIAS devices and applications, and HIAS IoT Agents. The AI Agents process incoming data by passing it through HIAS AI Models and returning the response back to the requesting device/application.

As with AI Models, AI Agents have an entry in the HIAS Context Broker and a JSON representation stored on the network.

You will now need to create your HIAS AI Agent and retrieve the credentials required by your GPT-3 Leukemia Information Assistant. Navigate to **AI->Agents->Create** to create a HIAS AI Model.

![HIAS AI Agent](../../assets/images/hias-ai-agent.jpg)

**MAKE SURE YOU SELECT THE PREVIOUSLY CREATED HIAS AI MODEL**

Once you have completed the form and submitted it, you can find the newly created AI Agent by navigating to **AI->Agents->List** and clicking on the relevant Agent.

On the HIAS AI Agent page you will be able to update the contextual data for the agent, and also find the JSON representation.

![HIAS AI Agent](../../assets/images/hias-ai-agent-edit.jpg)

You now need to download the credentials required to connect the GPT-3 Leukemia Information Assistant to the HIAS network.

Click on the **Agent Credentials** section to download the credentials file. This should open your file browser, navigate to the **GPT-3-Leukemia-Information-Assistant/configuration/** directory and save the file as **credentials.json**.

&nbsp;

# Continue
When you are ready to continue, activate your Anaconda environment:
```
 conda activate all-tfmkl
```
Now you can continue with the GPT-3 Leukemia Information Assistant [getting started guide](../getting-started.md)

&nbsp;

# Contributing

The Peter Moss Acute Myeloid & Lymphoblastic Leukemia AI Research project encourages and youlcomes code contributions, bug fixes and enhancements from the Github.

Please read the [CONTRIBUTING](../../CONTRIBUTING.md "CONTRIBUTING") document for a full guide to forking our repositories and submitting your pull requests. You will also find information about our code of conduct on this page.

## Contributors

- [Adam Milton-Barker](https://www.leukemiaresearchassociation.ai/team/adam-milton-barker "Adam Milton-Barker") - [Asociacion De Investigacion En Inteligencia Artificial Para La Leucemia Peter Moss](https://www.leukemiaresearchassociation.ai "Asociacion De Investigacion En Inteligencia Artificial Para La Leucemia Peter Moss") President/Founder & Lead Developer, Sabadell, Spain

&nbsp;

# Versioning

You use SemVer for versioning. For the versions available, see [Releases](../../releases "Releases").

&nbsp;

# License

This project is licensed under the **MIT License** - see the [LICENSE](../../LICENSE "LICENSE") file for details.

&nbsp;

# Bugs/Issues

You use the [repo issues](../../issues "repo issues") to track bugs and general requests related to using this project. See [CONTRIBUTING](../../CONTRIBUTING.md "CONTRIBUTING") for more info on how to submit bugs, feature requests and proposals.