# Communicative Agents for Software Development


## ⚡️ Quickstart

### 🖥️ Quickstart with terminal

To get started, follow these steps:

1. **Clone the GitHub Repository:** Begin by cloning the repository using the command:
   ```
   git clone https://github.com/toanctran/DevAgent.git
   ```
2. **Set Up Python Environment:** Ensure you have a version 3.9 or higher Python environment. You can create and
   activate this environment using the following commands, replacing `DevAgent_conda_env` with your preferred environment
   name:
   ```
   conda create -n ChatDev_conda_env python=3.9 -y
   conda activate ChatDev_conda_env
   ```
3. **Install Dependencies:** Move into the `DevAgent` directory and install the necessary dependencies by running:
   ```
   cd DevAgent
   pip3 install -r requirements.txt
   ```
4. **Set OpenAI API Key:** Export your OpenAI API key as an environment variable. Replace `"your_OpenAI_API_key"` with
   your actual API key. Remember that this environment variable is session-specific, so you need to set it again if you
   open a new terminal session.
   On Unix/Linux:
   ```
   export OPENAI_API_KEY="your_OpenAI_API_key"
   ```
   On Windows:
   ```
   $env:OPENAI_API_KEY="your_OpenAI_API_key"
   ```
5. **Build Your Software:** Use the following command to initiate the building of your software,
   replacing `[description_of_your_idea]` with your idea's description and `[project_name]` with your desired project
   name:
   On Unix/Linux:
   ```
   python3 run.py --task "[description_of_your_idea]" --name "[project_name]" --config "Default"
   ```
   On Windows:
   ```
   python run.py --task "[description_of_your_idea]" --name "[project_name]" --config "Default"
   ```
6. **Run Your Software:** Once generated, you can find your software in the `WareHouse` directory under a specific
   project folder, such as `project_name_DefaultOrganization_timestamp`. Run your software using the following command
   within that directory:
   On Unix/Linux:
   ```
   cd WareHouse/project_name_DefaultOrganization_timestamp
   python3 main.py
   ```
   On Windows:
   ```
   cd WareHouse/project_name_DefaultOrganization_timestamp
   python main.py
   ```
 