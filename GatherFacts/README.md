# Gathering Facts from the Devices
This project will be gathering the facts including Hostname, IP Address, Platform, OS Model, OS Version, Tunnel Lists, Media Type, and Connection Type.

## Description
we will have both CSV files of the gathered facts and also YAML format of them.

### How to Run
to reach the final output, you need to follow the orders that will be mentioned in the following:

#### Clone Repo
   ```bash
    git clone https://github.com/emomeni/CodeReview_Repo/tree/main/GatherFacts
    cd GatherFacts

#### Create venv

* first of all, you need to run the **datagathering.py**:
   ```bash
    python3 datagathering.py
* After the above section, we will have the CSV file including all of the data that we have gathered from the devices. the important notice that we need to consider is that we have Null cells in this csv file and we need to remove them. we can reach this goal by running the **nullremove.py** code.
   ```bash
    python3 nullremove.py
* and finally we need to convert the csv file to YAML format by running the **csv2yaml.py** code.
     ```bash
      python3 csv2yaml.py

### Install Requirements
